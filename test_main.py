"""
PySpark Application Test Suite for California Housing Data
"""
from pyspark.sql.session import SparkSession
import pytest
from lib.lib import (
    initiate_spark_session,
    read_dataset,
    describe,
    median_income_category,
)


@pytest.fixture(scope="session")
def spark_session():
    # Initialize a Spark session for testing
    session = initiate_spark_session("TestHousingDataProcessing")
    yield session
    # Stop the session after the tests are completed
    session.stop()


def test_data_loading(spark_session: SparkSession):
    # Test if data is loaded correctly
    data_path = "california_housing_train.csv"
    housing_df = read_dataset(spark_session, data_path)
    assert housing_df is not None and housing_df.count() > 0


def test_data_describe(spark_session: SparkSession):
    # Test if data description is working
    housing_df = read_dataset(spark_session, "california_housing_train.csv")
    description_data = describe(housing_df)
    assert description_data is not None


def test_data_transform(spark_session: SparkSession):
    # Test if the data transformation is applied correctly
    housing_df = read_dataset(spark_session, "california_housing_train.csv")
    transformed_housing_df = median_income_category(housing_df)
    assert transformed_housing_df is not None
    assert "IncomeCategory" in transformed_housing_df.columns


if __name__ == "__main__":
    # Directly invoking pytest.main() to run tests in this file
    pytest.main([__file__])
