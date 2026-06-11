# Databricks notebook source
# MAGIC %md
# MAGIC ###Load Table using path

# COMMAND ----------

df = spark.table("workspace.netflix.netflix_titles")

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC few basic Exploration

# COMMAND ----------

df_total_row = df.count()
print("total rows:", df_total_row)
print("Total Columns:", len(df.columns))

# COMMAND ----------

# MAGIC %md
# MAGIC ###Schema Inspection

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### sample records

# COMMAND ----------

df.limit(10).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###tempview

# COMMAND ----------

df.createOrReplaceTempView("netflix_raw")

# COMMAND ----------

# MAGIC %md
# MAGIC ###null analysis

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     SUM(CASE WHEN director IS NULL THEN 1 ELSE 0 END) AS director_nulls,
# MAGIC     SUM(CASE WHEN country IS NULL THEN 1 ELSE 0 END) AS country_nulls,
# MAGIC     SUM(CASE WHEN cast IS NULL THEN 1 ELSE 0 END) AS cast_nulls,
# MAGIC     SUM(CASE WHEN date_added IS NULL THEN 1 ELSE 0 END) AS date_added_nulls
# MAGIC FROM netflix_raw;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM netflix_raw
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ###movies vs shows

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     type, COUNT(*) AS total_title FROM netflix_raw
# MAGIC     GROUP BY type;

# COMMAND ----------

# MAGIC %md
# MAGIC ### bronze table

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE bronze_netflix AS
# MAGIC SELECT *
# MAGIC FROM netflix_raw;

# COMMAND ----------

# MAGIC %md
# MAGIC verifying

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_records
# MAGIC FROM bronze_netflix;