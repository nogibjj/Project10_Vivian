from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when
from pyspark.sql.types import StructType, StructField, DoubleType

REPORT_FILE = "report.md"

def append_to_report(description, content, sql_query=None):
    with open(REPORT_FILE, "a") as report:
        report.write(f"## {description}\n\n")
        if sql_query:
            report.write(f"**SQL Query:**\n```sql\n{sql_query}\n```\n\n")
        report.write("**Result:**\n\n")
        report.write(f"```markdown\n{content}\n```\n\n")

def initiate_spark_session(app_title):
    session = SparkSession.builder.appName(app_title).getOrCreate()
    return session

def read_dataset(spark, dataset_path):
    housing_schema = StructType([
        StructField("longitude", DoubleType(), True),
        StructField("latitude", DoubleType(), True),
        StructField("housing_median_age", DoubleType(), True),
        StructField("total_rooms", DoubleType(), True),
        StructField("total_bedrooms", DoubleType(), True),
        StructField("population", DoubleType(), True),
        StructField("households", DoubleType(), True),
        StructField("median_income", DoubleType(), True),
        StructField("median_house_value", DoubleType(), True),
    ])
    dataset = spark.read.option("header", True).schema(housing_schema).csv(dataset_path)
    append_to_report("Data Loading", dataset.limit(10).toPandas().to_markdown()) 
    return dataset

def describe(dataset):
    description = dataset.describe().toPandas().to_markdown()
    append_to_report("Data Description", description)
    return description

def median_income_category(dataset):
    income_conditions = [
        (col("median_income") <= 2.0),
        (col("median_income") <= 4.0),
        (col("median_income") <= 6.0),
    ]
    income_categories = ["Low Income", "Moderate Income", "High Income"]
    transformed_dataset = dataset.withColumn("IncomeCategory", when(
        income_conditions[0], income_categories[0]
        ).when(income_conditions[1], income_categories[1]
        ).when(income_conditions[2], income_categories[2]
        ).otherwise("Very High Income"))
    append_to_report("Income Category Transformation", 
                     transformed_dataset.limit(10).toPandas().to_markdown())
    return transformed_dataset

def execute_sql_query(spark, query, description):
    result = spark.sql(query)
    append_to_report(description, result.limit(10).toPandas().to_markdown(), sql_query=query)
    return result

# Initialize Spark Session
spark = initiate_spark_session("California Housing Data Analysis")

# Read in the dataset
housing_df = read_dataset(spark, "california_housing_train.csv")

# Describe the dataset
describe(housing_df)

# Register the DataFrame as a SQL temporary view
housing_df.createOrReplaceTempView("housing")

# SQL Query - Average total rooms by median income category
avg_rooms_sql = """
SELECT IncomeCategory, AVG(total_rooms) AS AvgTotalRooms
FROM (
    SELECT *, 
    CASE
        WHEN median_income <= 2 THEN 'Low Income'
        WHEN median_income <= 4 THEN 'Moderate Income'
        WHEN median_income <= 6 THEN 'High Income'
        ELSE 'Very High Income'
    END AS IncomeCategory
    FROM housing
)
GROUP BY IncomeCategory
ORDER BY IncomeCategory
"""

execute_sql_query(spark, avg_rooms_sql, "Average Total Rooms by Income Category")

# Transform the dataset by adding an Income Category
housing_with_income_cat = median_income_category(housing_df)

# Write the transformed DataFrame to a file
housing_with_income_cat.write.csv("transformed_housing_data.csv", header=True)

# Stop the Spark session
spark.stop()
