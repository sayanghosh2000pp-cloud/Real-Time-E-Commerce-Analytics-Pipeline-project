# Real-Time-E-Commerce-Analytics-Pipeline-project
Real-Time E-Commerce Analytics Pipeline project
RealTime_Ecommerce_Analytics/
│
├── README.md
├── requirements.txt
├── notebooks/
│   ├── 01_data_ingestion_kafka.ipynb
│   ├── 02_stream_processing_databricks.ipynb
│   ├── 03_batch_etl_adf.ipynb
│   └── 04_data_quality_checks.ipynb
├── src/
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   ├── spark_streaming_job.py
│   ├── batch_etl_job.py
│   └── data_validation.py
├── config/
│   ├── kafka_config.yaml
│   ├── databricks_config.json
│   └── adf_config.json
├── data/
│   ├── raw/
│   └── processed/
└── dashboards/
    └── powerbi_dashboard.pbix
