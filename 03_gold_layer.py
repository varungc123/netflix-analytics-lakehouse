# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold_content_type AS
# MAGIC
# MAGIC SELECT
# MAGIC     type,
# MAGIC     COUNT(*) AS total_titles
# MAGIC FROM silver_netflix
# MAGIC GROUP BY type;

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gold_content_type;

# COMMAND ----------

# MAGIC %md
# MAGIC ###Top Producing Countries

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold_country_analysis AS
# MAGIC
# MAGIC SELECT
# MAGIC     country,
# MAGIC     COUNT(*) AS total_titles
# MAGIC FROM silver_netflix
# MAGIC GROUP BY country
# MAGIC ORDER BY total_titles DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from gold_country_analysis;

# COMMAND ----------

# MAGIC %md
# MAGIC ###Total Content by Year

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold_yearly_content AS
# MAGIC
# MAGIC SELECT
# MAGIC     YEAR(date_added) AS year_added,
# MAGIC     COUNT(*) AS total_titles
# MAGIC FROM silver_netflix
# MAGIC WHERE date_added IS NOT NULL
# MAGIC GROUP BY YEAR(date_added)
# MAGIC ORDER BY year_added;

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from gold_yearly_content ;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Rating Distribution

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE gold_rating_distribution AS
# MAGIC
# MAGIC SELECT
# MAGIC     rating,
# MAGIC     COUNT(*) AS total_titles
# MAGIC FROM silver_netflix
# MAGIC GROUP BY rating
# MAGIC ORDER BY total_titles DESC;

# COMMAND ----------

# MAGIC %sql
# MAGIC Select * from gold_rating_distribution ;

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS tesla;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# MAGIC %md
# MAGIC ### DASHBOARD 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gold_content_type;

# COMMAND ----------

# MAGIC %md
# MAGIC ###Dashboard 2 — Top 10 Countries

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gold_country_analysis
# MAGIC ORDER BY total_titles DESC
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ###DASHBOARD 3 - Content per year

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM gold_yearly_content
# MAGIC ORDER BY year_added;