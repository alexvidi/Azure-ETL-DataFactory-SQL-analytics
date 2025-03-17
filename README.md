# Azure Data Engineering Project: Sales Data Pipeline

## Project Overview
This project demonstrates a **professional end-to-end data pipeline** using **Azure Data Services** to process and analyze sales data. The pipeline integrates multiple Azure services to ingest, transform, and store data for analytics.

## Technologies Used
- **Azure Storage Account**: Stores raw data in **Parquet format**.
- **Azure SQL Database**: Stores structured sales data for querying and analysis.
- **Azure Data Factory**: Orchestrates the ETL process.
- **Azure Data Studio**: Used for SQL querying and data validation.
- **Python**: Scripts for data ingestion and transformation.
- **GitHub**: Version control for project artifacts.

---
##  Project Structure
```
/AZURE_PROJECT_PIPELINE/
│── config/                           # Configuration settings
│   ├── config.py                      # Script for managing configurations
│── data/                              # Raw data storage
│   ├── products.parquet               # Sample dataset in Parquet format
│── images/                            # Screenshots for documentation
│   ├── azure_data_factory.png         # Azure Data Factory main dashboard
│   ├── container_azure.png            # Azure Blob Storage container
│   ├── file_upload_azure.png          # File upload process in Blob Storage
│   ├── mapping_azure_factory.png      # Schema mapping in Azure Data Factory
│   ├── pipeline_succeeded_azure.png   # Successful pipeline execution
│   ├── query_table_Azure_Data_Studio.png # Query execution in Azure Data Studio
│   ├── resources_azure.png            # Azure resource group overview
│   ├── sink_azure_factory.png         # Sink dataset configuration in Data Factory
│   ├── source_azure_factory.png       # Source dataset configuration in Data Factory
│   ├── sql_data_studio_structure.png  # SQL table structure in Azure Data Studio
│── notebooks/                         # Query results and analysis
│   ├── results_saved_query.csv        # Saved results from SQL queries
│── src/                               # Python scripts for data processing
│   ├── extract_data.py                # Extracts data from API
│   ├── upload_to_blob.py              # Uploads data to Azure Storage
│   ├── load_to_sql.py                 # Loads processed data into SQL Database
│── venv/                              # Virtual environment (excluded in .gitignore)
│── .env                               # Environment variables (excluded in .gitignore)
│── .gitignore                         # Git ignore file
│── README.md                          # Project documentation (this file)
│── requirements.txt                    # Python dependencies
```

---
##  End-to-End Data Pipeline Flow

### **1️ Data Ingestion**
- Data is extracted from a **public API** and stored in **Parquet format** inside **Azure Blob Storage**.
- **Python scripts** handle this step.

### **2️ Data Transformation & Load**
- **Azure Data Factory** moves the data from **Blob Storage** to **Azure SQL Database**.
- Data is transformed (schema mapping, data cleaning).

### **3️ Data Storage & Querying**
- The structured data is stored in **Azure SQL Database**.
- **Azure Data Studio** is used for SQL queries and analytics.

---
##  SQL Queries for Data Analysis
### **Top 5 Most Sold Categories**
```sql
SELECT category, COUNT(*) AS product_count
FROM products
GROUP BY category
ORDER BY product_count DESC
LIMIT 5;
```

### **Average Price per Category**
```sql
SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;
```

---
##  Deployment Steps
### **1️ Setup Azure Resources**
1. **Create an Azure Storage Account** (Blob Storage).
2. **Create an Azure SQL Database**.
3. **Create an Azure Data Factory instance**.

### **2️ Configure Data Pipeline**
1. Create **Linked Services** in **Azure Data Factory** (Storage & SQL).
2. Set up **Datasets** for Blob Storage (Parquet) and SQL.
3. Create a **Copy Activity** pipeline from **Blob Storage → SQL Database**.

### **3️ Run & Monitor Pipeline**
- **Trigger and execute pipeline** in **Azure Data Factory**.
- **Validate data in Azure SQL Database** using SQL queries.

---
##  Screenshots & Proof of Work
-  **Azure Data Factory Overview**
-  **Pipeline Design (Copy Data Activity)**
-  **Storage to SQL Mapping in Data Factory**
-  **SQL Queries in Azure Data Studio**

Find screenshots in the `images/` folder.

---
##  Key Takeaways
- **End-to-end Azure data pipeline with real-world use case.**
- **Integration of multiple Azure services professionally.**
- **Optimized for cloud-based data processing.**

---





