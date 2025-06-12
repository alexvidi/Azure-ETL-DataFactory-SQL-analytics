# Azure-Based ETL Pipeline & Power BI Analytics

## Overview

This repository delivers a robust, cloud-native ETL (Extract, Transform, Load) pipeline and analytics solution for product sales data. Leveraging **Python**, **Azure services** (Blob Storage, Data Factory, SQL Database), and **Power BI**, it demonstrates modern data engineering and business intelligence practices from ingestion to visualization.

---

## Features

- **Automated Data Extraction**: Retrieve product data from an external API and serialize it in Parquet format for efficient storage and processing.
- **Cloud Data Ingestion**: Securely upload raw Parquet files to Azure Blob Storage.
- **Orchestrated Transformation**: Use Azure Data Factory (ADF) to manage schema, transform data, and load it into Azure SQL Database.
- **SQL-Based Validation**: Explore and validate data using modular SQL scripts.
- **Business Intelligence**: Visualize key metrics (e.g., average price vs. rating by category) in an interactive Power BI dashboard.

---

## Solution Architecture

```mermaid
flowchart TD
    A[API (DummyJSON)] -->|Extract| B[Python Script<br/>(extract_data.py)]
    B -->|Save as Parquet| C[Raw Data<br/>(products.parquet)]
    C -->|Upload| D[Azure Blob Storage]
    D -->|Ingest| E[Azure Data Factory]
    E -->|Transform & Load| F[Azure SQL Database]
    F -->|Query| G[SQL Scripts<br/>(queries/)]
    F -->|Visualize| H[Power BI Dashboard<br/>(.pbix)]
```

---

## Repository Structure

```
Azure_Project_ETL_SQL_PowerBI/
├── config/                   # Configuration files
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
│   ├── extract_data.py
│   └── upload_to_blob.py
├── .env                      # Environment variables (not committed)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── .gitignore
```

---

## Prerequisites

- **Python 3.8+** and `pip`
- **Azure Subscription** with permissions for:
  - Blob Storage
  - Data Factory
  - SQL Database
- **Power BI Desktop** (for report development)

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/alexvidi/Azure_Project_ETL_SQL_PowerBI.git
cd Azure_Project_ETL_SQL_PowerBI
```

### 2. Set Up Python Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env` and populate with your Azure credentials:

```ini
STORAGE_ACCOUNT_NAME=...
STORAGE_ACCOUNT_KEY=...
CONTAINER_NAME=raw
SQL_SERVER=...
SQL_DATABASE=...
SQL_USERNAME=...
SQL_PASSWORD=...
```

---

## Running the ETL Pipeline

### 1. Extract Data

```bash
python src/extract_data.py
```
- Fetches product data from the API, cleans it, and writes `products.parquet` to `data/raw/`.


### 2. Upload to Azure Blob Storage

```bash
python src/upload_to_blob.py
```
- Uploads the Parquet file to your Azure Blob Storage container.

> **Note:** Data transformation and loading into SQL are orchestrated via Azure Data Factory.

---

## Azure Data Factory Orchestration

- **Linked Services**: Connect to Blob Storage and SQL Database.
- **Datasets**: Define Parquet source and SQL sink.
- **Data Flow**: Map schema and load into `dbo.products`.
- **Pipeline**: Automate the end-to-end ETL process.

After execution, validate with:

```sql
SELECT TOP 10 * FROM dbo.products;
```

---

## Power BI Analytics

- Open `reports/visual_average_price_rating.pbix` in Power BI Desktop.
- Refresh the data connection to Azure SQL Database.
- Explore the "Average Price and Average Rating by Product Category" visualization.

---

## SQL Query Library

Located in `queries/`:

- `avg_price_by_category.sql`
- `top_rated_products.sql`
- `products_low_stock.sql`

Use these scripts in Azure Data Studio or the SQL Query Editor for further analysis.

---

## Next Steps

- Enhance transformation logic in ADF Data Flows.
- Schedule automated pipeline runs.
- Expand Power BI dashboards with additional metrics and filters.

---

## Author

**Alexandre Vidal**  
[alexvidaldepalol@gmail.com](mailto:alexvidaldepalol@gmail.com)  
[LinkedIn](https://www.linkedin.com/in/alex-vidal-de-palol-a18538155/)  
[GitHub](https://github.com/alexvidi)

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.






