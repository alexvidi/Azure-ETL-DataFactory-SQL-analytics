##  Project Overview

This repository implements a **cloud‑based ETL pipeline** and visualization layer for product sales data. It demonstrates end‑to‑end data engineering best practices using **Python**, **Azure services** (Blob Storage, Data Factory, SQL Database) and **Power BI** for reporting.

### Key Features

* **Extract**: Fetch product data from an external API and store in Parquet format using Python.
* **Load to Cloud**: Upload raw Parquet files to Azure Blob Storage securely.
* **Orchestrate & Transform**: Use Azure Data Factory (ADF) to read the Parquet source, apply schema management, and load into Azure SQL Database.
* **Data Validation & Queries**: Store a set of SQL scripts for exploration and validation in the `queries/` folder.
* **Visualization**: Build an insightful Power BI report displaying average price vs. rating by category.

##  Repository Structure

```
Azure_Project_ETL_SQL_PowerBI/
├── config/                  
├── data/
│   └── raw/
│       └── products.parquet  # Extracted Parquet dataset
├── queries/                  # SQL scripts for data exploration
│   ├── avg_price_by_category.sql
│   ├── top_rated_products.sql
│   └── products_low_stock.sql
├── reports/                  # Power BI artifacts and exports
│   ├── visual_average_price_rating.pbix
│   ├── visual_average_price_rating.pbit
│   └── visual_average_price_rating.pdf
├── src/                      # ETL Python scripts
│   ├── extract_data.py       # Extract from API, clean, save Parquet
│   └── upload_to_blob.py     # Upload Parquet to Azure Blob Storage
├── .env                      # Environment variables 
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation
└── .gitignore
```

## Prerequisites

* **Python 3.8+** with `pip` installed
* **Azure Subscription** with permissions to create:

  * Storage Account (Blob)
  * Data Factory
  * SQL Database
* **Power BI Desktop** for report development

## Setup & Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/alexvidi/Azure_Project_ETL_SQL_PowerBI.git
   cd Azure_Project_ETL_SQL_PowerBI/src
   ```
2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate       # Windows
   ```
3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables**:

   * Copy `.env.example` to `.env` and fill in your Azure credentials:

     ```ini
     STORAGE_ACCOUNT_NAME=...
     STORAGE_ACCOUNT_KEY=...
     CONTAINER_NAME=raw
     SQL_SERVER=...
     SQL_DATABASE=...
     SQL_USERNAME=...
     SQL_PASSWORD=...
     ```

## Running the Pipeline Locally

1. **Extract & Save**:

   ```bash
   python extract_data.py
   ```

   * Fetches API data, cleans nested columns, writes `products.parquet` to `../data/raw/`.
2. **Upload to Blob**:

   ```bash
   python upload_to_blob.py
   ```

   * Uploads the Parquet file to your Azure Blob Storage container.

> **Note**: Transformation and loading into SQL are performed in Azure Data Factory.

## Azure Data Factory Orchestration

1. **Linked Services**:

   * Connect to Azure Blob Storage and Azure SQL Database using account keys.
2. **Datasets**:

   * Parquet source: `dataset_parquet`
   * SQL sink: `ds_sql_products`
3. **Data Flow**: `df_parquet_to_sql_products`

   * Reads Parquet, maps schema, loads into `dbo.products` table.
4. **Pipeline**: `etl_products`

   * Triggers the Data Flow for an end‑to‑end run.

After running in **Debug** or with a trigger, verify results in the **Query editor**:

```sql
SELECT TOP 10 *
FROM dbo.products;
```

## Power BI Report

The report file `reports/visual_average_price_rating.pbix` contains a single, impactful visualization:

* **Average Price and Average Rating by Product Category**

### How to view

1. Open the PBIX in Power BI Desktop.
2. Refresh data connection to Azure SQL Database.
3. Explore the combined line & column chart.

## SQL Queries for Exploration

Stored in `queries/`:

* `avg_price_by_category.sql`
* `top_rated_products.sql`
* `products_low_stock.sql`

Run these in Azure Data Studio or Query Editor for deeper insights.

## Next Steps

* Implement additional transforms in ADF Data Flows.
* Schedule pipeline runs with ADF triggers.
* Expand Power BI dashboard with new visuals and slicers.

---


## Author

**Alexandre Vidal**  
[alexvidaldepalol@gmail.com](mailto:alexvidaldepalol@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/alex-vidal-de-palol-a18538155/)  
[GitHub](https://github.com/alexvidi)

**Project Repository:** [Azure_Project_ETL_SQL_PowerBI](https://github.com/alexvidi/Azure_Project_ETL_SQL_PowerBI)

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.






