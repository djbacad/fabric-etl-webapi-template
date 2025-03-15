# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "e811e32b-c118-48bd-a916-d150795c239b",
# META       "default_lakehouse_name": "DJBGLOBALSTATSLH001",
# META       "default_lakehouse_workspace_id": "82bf7c21-a118-4085-8021-659a46a298a9"
# META     },
# META     "environment": {
# META       "environmentId": "8d93a6fa-6a87-bda2-4a64-2929f6f51929",
# META       "workspaceId": "00000000-0000-0000-0000-000000000000"
# META     }
# META   }
# META }

# MARKDOWN ********************

# ### Import Libraries

# CELL ********************

from dotenv import load_dotenv
import requests
import json
import os
import pandas as pd
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, ArrayType

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Specify API Key

# CELL ********************

load_dotenv("./env/.env")

# Retrieve the API key
API_KEY = os.getenv("OPENAQ_API_KEY")
headers = {"X-API-Key": API_KEY}

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Step 1: Fetch the list of available countries from OpenAQ

# CELL ********************

countries_url = "https://api.openaq.org/v3/countries"
response = requests.get(countries_url, headers=headers)
countries_data = response.json()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Step 2: Fetch all corresponding air quality metrics

# CELL ********************

countries_list = []
for country in countries_data.get("results", []):
    countries_list.append({
        "id": country.get("id"),
        "code": country.get("code"),
        "name": country.get("name"),
        "datetimeFirst": country.get("datetimeFirst"),
        "datetimeLast": country.get("datetimeLast"),
        "parameters": [param["name"] for param in (country.get("parameters") or []) if isinstance(param, dict)]
    })

# Convert to Pandas DataFrame
countries_df = pd.DataFrame(countries_list)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Step 3: Convert to Spark DF

# CELL ********************

schema = StructType([
    StructField("id", StringType(), True),
    StructField("code", StringType(), True),
    StructField("name", StringType(), True),
    StructField("datetimeFirst", StringType(), True),
    StructField("datetimeLast", StringType(), True),
    StructField("parameters", ArrayType(StringType()), True) 
])
spark_countries_df = spark.createDataFrame(countries_df, schema=schema)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

spark_countries_df.show()

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Save as Table in LH

# CELL ********************

table_name = "aq_metrics"
spark_countries_df.write.mode("overwrite").saveAsTable(f"`DJBGLOBALSTATSLH001`.`dbo`.`{table_name}`")
print(f"✅ Successfully saved {table_name} in your Lakehouse!")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
