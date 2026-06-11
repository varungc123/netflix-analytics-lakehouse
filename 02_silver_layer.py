# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT
# MAGIC     SUM(CASE WHEN show_id IS NULL THEN 1 ELSE 0 END) AS show_id_nulls,
# MAGIC     SUM(CASE WHEN type IS NULL THEN 1 ELSE 0 END) AS type_nulls,
# MAGIC     SUM(CASE WHEN title IS NULL THEN 1 ELSE 0 END) AS title_nulls,
# MAGIC     SUM(CASE WHEN director IS NULL THEN 1 ELSE 0 END) AS director_nulls,
# MAGIC     SUM(CASE WHEN cast IS NULL THEN 1 ELSE 0 END) AS cast_nulls,
# MAGIC     SUM(CASE WHEN country IS NULL THEN 1 ELSE 0 END) AS country_nulls,
# MAGIC     SUM(CASE WHEN date_added IS NULL THEN 1 ELSE 0 END) AS date_added_nulls,
# MAGIC     SUM(CASE WHEN release_year IS NULL THEN 1 ELSE 0 END) AS release_year_nulls,
# MAGIC     SUM(CASE WHEN rating IS NULL THEN 1 ELSE 0 END) AS rating_nulls,
# MAGIC     SUM(CASE WHEN duration IS NULL THEN 1 ELSE 0 END) AS duration_nulls,
# MAGIC     SUM(CASE WHEN listed_in IS NULL THEN 1 ELSE 0 END) AS listed_in_nulls,
# MAGIC     SUM(CASE WHEN description IS NULL THEN 1 ELSE 0 END) AS description_nulls
# MAGIC FROM bronze_netflix;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE silver_netflix AS
# MAGIC
# MAGIC SELECT DISTINCT
# MAGIC     show_id,
# MAGIC     type,
# MAGIC     title,
# MAGIC
# MAGIC     COALESCE(director,'Unknown') AS director,
# MAGIC     COALESCE(cast,'Unknown') AS cast,
# MAGIC     COALESCE(country,'Unknown') AS country,
# MAGIC
# MAGIC     TO_DATE(TRIM(date_added), 'MMMM d, yyyy') AS date_added,
# MAGIC
# MAGIC     release_year,
# MAGIC
# MAGIC     COALESCE(rating,'Unknown') AS rating,
# MAGIC     COALESCE(duration,'Unknown') AS duration,
# MAGIC     COALESCE(listed_in,'Unknown') AS listed_in,
# MAGIC     COALESCE(description,'Unknown') AS description
# MAGIC
# MAGIC FROM bronze_netflix
# MAGIC
# MAGIC WHERE show_id IS NOT NULL
# MAGIC   AND type IS NOT NULL
# MAGIC   AND title IS NOT NULL
# MAGIC   AND release_year IS NOT NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE silver_netflix;

# COMMAND ----------

# MAGIC %md
# MAGIC ### verify total records

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) AS total_records
# MAGIC FROM silver_netflix;

# COMMAND ----------

# MAGIC %md ###verify null records

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     SUM(CASE WHEN director IS NULL THEN 1 ELSE 0 END) AS director_nulls,
# MAGIC     SUM(CASE WHEN cast IS NULL THEN 1 ELSE 0 END) AS cast_nulls,
# MAGIC     SUM(CASE WHEN country IS NULL THEN 1 ELSE 0 END) AS country_nulls,
# MAGIC     SUM(CASE WHEN rating IS NULL THEN 1 ELSE 0 END) AS rating_nulls
# MAGIC FROM silver_netflix;

# COMMAND ----------

# MAGIC %md
# MAGIC ### data validation

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver_netflix
# MAGIC LIMIT 20;

# COMMAND ----------

# MAGIC %md
# MAGIC ###data quality summary

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(DISTINCT show_id) AS unique_titles
# MAGIC FROM silver_netflix;