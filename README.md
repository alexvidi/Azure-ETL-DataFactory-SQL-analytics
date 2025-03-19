# Cloud-Based ETL Pipeline: Transforming Sales Data with Azure & Power BI

## Project Overview

This project demonstrates a professional end-to-end data pipeline leveraging Azure Data Services to process and analyze sales data efficiently. The pipeline is designed to handle data ingestion, transformation, and visualization while ensuring best practices in data engineering.

The objective of this project is to build a scalable and structured ETL (Extract, Transform, Load) pipeline that ingests sales data from an external source, processes it using Azure Data Factory, and stores the refined data in Azure SQL Database. The processed data is then visualized in Power BI to generate insightful business analytics.

## Architecture Workflow

# End-to-End Data Pipeline Flow

**1️ Data Ingestion**

* Data is extracted from an external Parquet dataset and stored in Azure Blob Storage.
* Python scripts handle the ingestion and loading process.

**2️ Data Transformation & Load**

* Azure Data Factory orchestrates the ETL process:
    * Data is extracted from Azure Blob Storage.
    * Data is transformed using Data Flows:
        * Category Standardization for consistent classification.
        * Stock Status Classification to indicate inventory levels.
        * Product Popularity Segmentation based on sales and availability.
        * Data Type Conversions to match SQL schema.
    * The cleaned data is loaded into Azure SQL Database.

**3️ Data Storage & Querying**

* Azure SQL Database stores the transformed and structured data.
* Azure Data Studio is used for SQL querying, validation, and analysis.

**4️ Data Visualization**

* Power BI is used to create dashboards with key business insights.
* Reports include:
    * Stock Status Distribution
    * Average Price per Category
    * Product Popularity by Category
* Reports are stored in .pbix and .pdf formats.

## Technologies Used

* **Azure Storage Account:** Stores raw sales data in Parquet format.
* **Azure Data Factory:** Manages ETL processes for data transformation.
* **Azure SQL Database:** Stores structured sales data for querying and analytics.
* **Azure Data Studio:** SQL querying and data validation.
* **Power BI:** Interactive dashboards and business intelligence reports.
* **Python:** Custom scripts for data extraction and ingestion.
* **GitHub:** Version control and project repository management.

---
##  Project Structure
```
/azure-sales-pipeline/
│── config/                          # Configuration files
│   ├── config.py                     # Main configuration script
│
│── data/                             # Data storage
│   ├── processed/                     # Processed data
│   │   ├── Results_pipeline_sql_data_studio.csv  # Processed results from SQL Data Studio
│   ├── raw/                           # Raw data
│   │   ├── products.parquet            # Original dataset
│
│── images/                           # Project-related images
│   ├── azure_data_factory/             # Azure Data Factory images
│   │   ├── azure_data_studio_validate_pipeline.png  # Validation of pipeline in Data Studio
│   │   ├── data_flow_etl_estructure.png  # Data Flow ETL process structure
│   │   ├── pipeline_activity_dataflow_succeeded.png  # Successful Dataflow pipeline execution
│   ├── azure_data_studio_sql/          # Azure Data Studio SQL queries
│   │   ├── azure_data_studio_queries.png  # Queries executed in Azure Data Studio
│
│── reports/                          # Reports generated from data analysis
│   ├── power_bi/                       # Power BI reports
│   │   ├── Sales_Analytics_Report.pbix  # Power BI report file
│   │   ├── Sales_Analytics_Report.pdf   # Exported report in PDF format
│
│── src/                              # Source code for data processing
│   ├── extract_data.py                 # Script to extract data from the source
│   ├── load_to_sql.py                   # Script to load data into SQL
│   ├── upload_to_blob.py                 # Script to upload data to Azure Blob Storage
│
│── venv/                             # Virtual environment for dependencies
│
│── .env                              # Environment variables configuration
│── .gitignore                        # Git ignore file
│── README.md                         # Project documentation
│── requirements.txt                   # Python dependencies list               
```

---

# Deployment Steps

**1️ Setup Azure Resources**

* Create an Azure Storage Account (Blob Storage) for raw data.
* Deploy an Azure SQL Database to store structured data.
* Set up Azure Data Factory for ETL orchestration.

**2️ Configure Data Pipeline**

* Create Linked Services in Azure Data Factory (Blob Storage & SQL).
* Define Datasets for Parquet data (raw) and SQL Database (structured).
* Implement a Data Flow Activity pipeline to:
    * Extract from Blob Storage.
    * Transform data (Data Flow Transformations).
    * Load cleaned data into Azure SQL Database.

**3️ Run & Monitor Pipeline**

* Trigger the ETL pipeline in Azure Data Factory.
* Monitor execution status in the ADF UI.
* Validate the processed data using SQL queries in Azure Data Studio.

## Screenshots & Proof of Work

* Azure Data Factory Pipeline Execution
* Data Flow Transformations
* SQL Data Validation in Azure Data Studio
* Power BI Reports and Dashboards

All screenshots are stored in the `images/` folder under:

* `images/azure_data_factory/`
* `images/azure_data_studio_sql/`
* `reports/power_bi/`

---








