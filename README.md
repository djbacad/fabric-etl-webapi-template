# Fabric ETL Web API Template
***

### Overview
This is a template project demonstrating **ETL pipelines** using **Microsoft Fabric** to ingest data from **Web APIs**. We showcase two ingestion methods:

1. **Dataflows Gen2** – A low-code approach using Power Query to extract and transform API data.
2. **Spark Notebooks** – A scalable method using PySpark to process and store data.
3. 

The demo ingests:
- **Air Quality Metrics** from OpenAQ API
- **COVID-19 Statistics** from Disease.sh API

This project is built on a **Fabric Free Trial** workspace.

---

### Sample Screenshots
#### Dataflow Gen2 Ingestion
![dataflow_gen2](https://github.com/user-attachments/assets/67d85104-e50d-44ef-ada3-4c30a2d78596)

#### Spark Notebook Ingestion
![spark_notebook](https://github.com/user-attachments/assets/38a6c923-e291-4cf1-812c-d6b07572f163)


#### Simple Pipeline
![PL](https://github.com/user-attachments/assets/25a31820-efe2-4ddf-8744-f304e89f4d0d)


### Features
- **Two ETL Methods:** Use either **Dataflows Gen2** or **Spark Notebooks** to ingest data.
- **API Data Extraction:** Fetch live **Air Quality** and **COVID-19** data from open sources.
- **Transformation:** Convert timestamp fields, extract parameters, and clean data.
- **Lakehouse Storage:** Store structured data in Microsoft Fabric Lakehouse tables.
- **Environment Management:** Use a **custom Spark environment** to install dependencies.
---

