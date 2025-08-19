Weather & E-commerce Data Pipeline
This project establishes a comprehensive data pipeline for an e-commerce business, integrating weather data to generate actionable insights and key performance indicators (KPIs) related to delivery logistics and agricultural advisories.

Table of Contents
Project Overview

Data Sources & Model

Data Pipeline Design

Calculated Metrics & KPIs

Deliverables

1. Project Overview
The goal of this project is to move from raw data to actionable business intelligence. We achieve this by:

Integrating disparate data sources (weather, e-commerce orders) into a single, cohesive database.

Automating the data collection and transformation process using a workflow orchestrator.

Calculating key metrics and KPIs that directly inform business decisions.

Visualizing the results in an easy-to-understand dashboard.

2. Data Sources & Model
Data Sources
Weather Forecasts: Contains granular weather data including rainfall, wind speed, and temperature in Kelvin. This data is the foundation for all weather-related risk assessments.

E-commerce Orders: Holds details about customer orders, including delivery times, cancellations, and product information.

Data Model
The data model is a relational design in a PostgreSQL database, with normalized tables for weather, products, orders, and locations. This structure ensures data integrity and allows for efficient querying and joining of information.

3. Data Pipeline Design
The data pipeline is designed as a daily ETL (Extract, Transform, Load) process, orchestrated by an Apache Airflow DAG. This ensures the data is fresh and the metrics are always up-to-date.

The Airflow DAG is composed of the following tasks:

Data Ingestion: A Python script connects to APIs and other sources to extract the latest weather and e-commerce data and load it into staging tables.

Data Transformation: A series of SQL queries clean, merge, and transform the raw data from the staging tables into a final, clean data model.

Metric Calculation: Another series of SQL queries compute all of the project's key metrics and KPIs, saving them into dedicated tables for fast dashboard loading.

Data Validation: A final task runs a set of checks to ensure the data is complete and accurate before the pipeline concludes.

4. Calculated Metrics & KPIs
This project generates several key metrics and KPIs, divided into two main categories:

E-commerce & Logistics KPIs
Daily Rainfall (mm): Total daily rainfall per city.

Rain Risk Flag: A flag indicating "High Rain Risk" if daily rainfall is ≥ 5mm or there are ≥ 3 hours of rain.

Wind Risk Flag: A flag indicating "High Wind Risk" if average daily wind speed is ≥ 10 m/s.

Delivery Risk Index: A combined metric that flags "High Delivery Risk" if either the Rain or Wind Risk is high.

Agriculture KPIs
7-Day Cumulative Rainfall (mm): The total rainfall over a rolling 7-day period, critical for assessing soil moisture.

Planting Window Flag: A flag indicating an "Ideal Planting Window" if the 7-day cumulative rainfall is ≥ 20mm and the average daily temperature (converted from Kelvin to Celsius) is within an optimal range (18-24°C).

Weather Risk to Crops: A flag that identifies "Heavy Rain Risk" (≥ 15mm), "High Wind Risk" (≥ 15 m/s), or "Heat Stress Risk" (average temperature ≥ 25°C).

5. Deliverables
Project Report: A detailed document explaining the entire project lifecycle, from data sources to the final analysis.

Automated Data Pipeline: The production-ready Airflow DAG that automates the daily data process.

Final Power BI Dashboard: The end-user visualization tool that displays the operations, weather, sales, and agricultural advisories based on the generated KPIs.