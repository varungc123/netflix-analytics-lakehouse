# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT
# MAGIC     SUM(CASE WHEN show_id IS NULL THEN 1 ELSE 0 END) AS null_show_id,
# MAGIC     SUM(CASE WHEN title IS NULL THEN 1 ELSE 0 END) AS null_title
# MAGIC FROM silver_netflix;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM silver_netflix
# MAGIC WHERE date_added IS NULL;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     COUNT(*) AS total_records,
# MAGIC     COUNT(DISTINCT show_id) AS unique_records
# MAGIC FROM silver_netflix;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE DETAIL silver_netflix;