# Retail Data Engineering Pipeline

## Overview

This project focuses on building an end-to-end retail data engineering pipeline using Python, Pandas and Microsoft SQL Server.

The objective is to develop practical skills in data extraction, data quality validation, transformation and database loading.

## Technologies

- Python
- Pandas
- SQL Server
- T-SQL
- PyODBC
- Git and GitHub

## Pipeline Architecture

CSV Files → Python Extraction → Data Validation & Cleaning → Data Quality Checks → SQL Server Staging

## Current Progress

### 1. Environment Setup
- Configured Python virtual environment.
- Installed Pandas, SQLAlchemy, PyODBC and Requests.
- Structured the project directory.

### 2. Data Extraction
- Read retail transaction data from CSV files using Pandas.
- Inspected dataset structure and data types.

### 3. Data Quality & Validation
- Identified missing values and duplicate records.
- Converted columns into appropriate data types.
- Implemented validation rules for quantity, price and customer information.
- Separated valid records from quarantined records.
- Generated a data quality report.

### 4. SQL Server Integration
- Established a Python connection to SQL Server using Windows Authentication.
- Created a staging table.
- Successfully loaded validated records into SQL Server.

## Upcoming Improvements

- Implement batch inserts using `executemany()`.
- Improve database loading performance.
- Implement error handling and logging.
- Develop SQL transformation procedures.
- Introduce rerunnable and idempotent loading.
- Document the complete pipeline architecture.

## Project Status

Work in progress.
