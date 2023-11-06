# README [![CI](https://github.com/nogibjj/Project10_Vivian/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Project10_Vivian/actions/workflows/ci.yml)

This repository features the materials for Mini-Project 10. It includes: 
- A Makefile
- A Dockerfile
- A foundational set of libraries for development operations and web applications
- GitHub Actions
- A library of functions to perform Spark SQL
- main.py and test_main.py

## Purpose Of Project
This project documents the data processing and analysis performed on the California housing dataset using PySpark. The analysis aimed to leverage the distributed computing capabilities of Spark to handle large volumes of data efficiently.

The California housing dataset comprises several attributes related to the housing demographics of the region. PySpark, an interface for Apache Spark in Python, was utilized to conduct exploratory data analysis, transform the data, and perform a query using Spark SQL.

### Data Overview
The dataset contains the following attributes, all of which are of type double:
- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Median House Value

## Preparation 
1. open the project in codespaces
2. container built and virtual environment to activated through requirements.txt

## Check Format & Errors
1. make format
2. make lint

<img width="579" alt="Screen Shot 2023-11-05 at 10 13 28 PM" src="https://github.com/nogibjj/Project10_Vivian/assets/143654445/14d59db7-6014-4ed9-a7c1-6faff592df71">


4. make test

<img width="702" alt="Screen Shot 2023-11-05 at 10 13 01 PM" src="https://github.com/nogibjj/Project10_Vivian/assets/143654445/9ee9d1c7-df00-4c29-872e-4f66e69aac45">


## functionalities
- Initialization: Starts a new Spark session.
- Data Loading: Reads the california_housing_train.csv dataset with predefined schema.
- Data Description: Generates a statistical summary of the data.
- Data Transformation: Categorizes median_income into different categories.
    - median_income_category:Uses Spark SQL functions to create a new column called IncomeCategory based on the conditions set for the median_income column. It applies the when function, which is similar to the SQL CASE WHEN statement, to categorize incomes. The transformed DataFrame is then returned and a preview of it is added to the report.
- SQL Query Execution: Performs a Spark SQL query to get average total_rooms by the newly created IncomeCategory.

## Output
The transformation and queries yielded the following results:
- A summary of the descriptive statistics.
- A preview of the data with the new `IncomeCategory` column.
- The count of houses per income category.
Detailed queries and outputs are shown in [report.md](https://github.com/nogibjj/Project10_Vivian/blob/c7abbfa538c86c8cb0e3fd0cc29f6a1b16a29c9e/report.md)
