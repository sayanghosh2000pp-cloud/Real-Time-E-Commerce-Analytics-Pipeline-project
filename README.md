# Real-Time E-Commerce Analytics Pipeline on Azure

## Project Overview
Scalable end-to-end data pipeline for e-commerce transactions using **Azure Cloud**, **Kafka**, **Databricks**, and **ADF**.

## Technologies Used
Python, PySpark, Apache Kafka, Azure Data Factory, Azure Databricks, Azure Data Lake, Azure SQL, Power BI, Git, Unix Shell

## Project Structure
- src/: Python scripts (producer, consumer, streaming, batch, validation)
- notebooks/: Jupyter notebooks
- config/: configuration files
- data/: raw and processed data
- dashboards/: Power BI dashboards

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Start Kafka broker and run producer.
3. Execute Spark streaming job on Databricks.
4. Orchestrate batch ETL via ADF.
5. Visualize processed data in Power BI.
