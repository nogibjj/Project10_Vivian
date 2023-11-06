from lib.lib import (
    initiate_spark_session,
    read_dataset,
    describe,
    median_income_category,
    execute_sql_query,
)


def run_data_analysis():
    # Start Spark session
    spark = initiate_spark_session("California Housing Data Analysis")

    # Path to the housing dataset
    data_file_path = "california_housing_train.csv"

    # Read the housing dataset into a Spark DataFrame
    housing_data = read_dataset(spark, data_file_path)

    # Get a descriptive statistics report of the data
    describe(housing_data)

    # Transform the data by categorizing the 'median_income'
    transformed_data = median_income_category(housing_data)

    # Register the DataFrame as a temporary SQL view
    transformed_data.createOrReplaceTempView("housing_data_view")

    # Define a SQL query to calculate the average house value by income category
    sql_query = """
        SELECT IncomeCategory, AVG(median_house_value) AS AverageHouseValue
        FROM housing_data_view
        GROUP BY IncomeCategory
        ORDER BY AverageHouseValue DESC
    """

    # Execute the SQL query and get the result
    query_result = execute_sql_query(
        spark, sql_query, "Average House Value by Income Category"
    )

    # Display the query result in the console
    query_result.show()

    # Optionally, save the query result to a CSV file
    # query_result.write.format("csv").save("output/query_result.csv")

    # Stop the Spark session
    spark.stop()


if __name__ == "__main__":
    run_data_analysis()
