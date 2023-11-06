# README [![CI](https://github.com/nogibjj/Project4_Vivian/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Project4_Vivian/actions/workflows/ci.yml)

This repository features the materials for Mini-Project 4. It includes: 
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
3. passed all 3 versions python build

<img width="1313" alt="Screen Shot 2023-09-21 at 5 14 27 PM" src="https://github.com/nogibjj/Project4_Vivian/assets/143654445/098da71b-ffa9-490f-83a8-3e37abef63f1">


## Check Format & Errors
1. make format
2. make lint

<img width="507" alt="Screen Shot 2023-09-21 at 5 08 39 PM" src="https://github.com/nogibjj/Project4_Vivian/assets/143654445/3f7de37e-b25b-4732-911c-6eceedb7b046">

4. make test

<img width="1071" alt="Screen Shot 2023-09-21 at 5 08 28 PM" src="https://github.com/nogibjj/Project4_Vivian/assets/143654445/6a30d369-56af-4fc9-b6e0-96517d80b08b">


## functionalities
In lib/lib.py
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
Detailed queris and outputs are shown in report.md. 
