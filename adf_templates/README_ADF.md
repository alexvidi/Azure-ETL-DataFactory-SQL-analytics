# Azure Data Factory – Exported ARM Templates

This folder contains the exported ARM templates and deployment files from the Azure Data Factory instance **alexvidi-adf-sales-pipeline**.  
They describe the full ETL process used to ingest Parquet data from Azure Blob Storage, transform it in Data Flows, and load it into **Azure SQL Database (sales_data_db)**.

---

## Folder Structure

- **factory_base/** → defines the Data Factory resource and managed identity.
- **pipeline_deployment/** → contains the linked services, datasets, dataflow, and pipeline configurations.
- **master_deployment/** → orchestrates deployment using the master and linked ARM templates.
- **images/** → includes exported visual diagrams of the Data Flow and Pipeline structure.

---

## Deployment Command Example

You can redeploy this Data Factory by running:

```bash
az deployment group create \
  --resource-group data-lake-rg \
  --template-file master_deployment/ArmTemplate_master.json \
  --parameters @master_deployment/ArmTemplateParameters_master.json \
  --parameters factoryName="alexvidi-adf-sales-pipeline"

