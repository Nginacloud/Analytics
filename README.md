# Weather & E-commerce Data Pipeline

This project establishes a comprehensive data pipeline for an e-commerce business, integrating weather data to generate actionable insights and key performance indicators (KPIs) related to delivery logistics and agricultural advisories.

[DATA](DATA) folder has all csv files extracted fom various sources.
[SCRIPTS](SCRIPTS) folder has all sql and python scripts executed to get the results we now have.


**Table of Contents**
Project Overview

Data Sources & Model

Data Pipeline Design

Calculated Metrics & KPIs

Deliverables

## 1. Project Overview

The goal of this project is to move from raw data to actionable business intelligence by:

    Integrating  data sources (weather, e-commerce products , product users and orders) into a single, database.

    Processing the data using well-documented, SQL scripts due to technical challenges with automated scheduling tools.

    Calculating key metrics and KPIs that directly inform business decisions.

    Visualizing the results in a power-bi dashboard.

## 2. Data Sources

**Data Sources**
- [Weather_Forecasts](https://github.com/Nginacloud/Analytics/blob/main/SCRIPTS/weatherapi.py): Contains granular weather data including rainfall, wind speed, and temperature. This data is the foundation for all weather-related risk assessments. [OpenWeatherMap](https://openweathermap.org/api)

- E-commerce [Products](https://github.com/Nginacloud/Analytics/blob/main/SCRIPTS/products.py): Holds details about product names and prices. [zucchini online buy](https://zucchini.co.ke/?srsltid=AfmBOopP4C6-78MEELvkAv5f3-kInduNAB24-7udXa_IdbOZbeGQ4GYk)

- [Users](https://github.com/Nginacloud/Analytics/blob/main/SCRIPTS/users.py): Has data on the individuals making orders from the 5 cities.[fakerapi](https://fakerapi.it/fake-data-download)

- E-commerce [Orders](https://github.com/Nginacloud/Analytics/blob/main/SCRIPTS/orders.py): Holds details about customer orders, delivery times, and cancellations 0 being not cancelled. For this I did randomisation from the csv files i already had, products and users. They did not have unique keys so i randomises product and user ids for ease in relating


## 3. Data Pipeline Design
The data pipeline is designed as an ETL (Extract, Transform, Load) process. While a workflow orchestrator was the initial plan, this version uses SQL scripts for the core data transformation and metric calculation steps.

The pipeline is composed of the following steps:

Data extraction: Python scripts connecting to APIs and other sources to extract the latest [weather](https://github.com/Nginacloud/Analytics/blob/main/DATA/weather_forecasts.csv), [products](https://github.com/Nginacloud/Analytics/blob/main/DATA/products.csv) and [user](https://github.com/Nginacloud/Analytics/blob/main/DATA/users.csv) data and load it into csv files.

Data Transformation: A series of SQL queries clean, merge, and transform the raw data from the staging tables into a final, clean data model.
The result is exported to a csv file for further analysis/insights. [Exported_data](https://github.com/Nginacloud/Analytics/blob/main/DATA/Exported%20data%20from%20sql%20merge%20result.csv)

Metric Calculation: Another series of SQL queries compute all of the project's key metrics and KPIs.


## 4. Calculated Metrics & KPIs
This project generates several key [metrics and KPIs](https://github.com/Nginacloud/Analytics/blob/main/SCRIPTS/KPIs%20and%20metric%20calculations.sql), divided into:

E-commerce & Logistics KPIs
Daily Rainfall (mm): Total daily rainfall per city.

Rain Risk Flag: A flag indicating "High Rain Risk" if daily rainfall is ≥ 5mm or there are ≥ 3 hours of rain.

Wind Risk Flag: A flag indicating "High Wind Risk" if average daily wind speed is ≥ 10 m/s.

Delivery Risk Index: A combined metric that flags "High Delivery Risk" if either the Rain or Wind Risk is high.

Agriculture KPIs
7-Day Cumulative Rainfall (mm): The total rainfall over a rolling 7-day period, critical for assessing soil moisture.

Planting Window Flag: A flag indicating an "Ideal Planting Window" if the 7-day cumulative rainfall is ≥ 20mm and the average daily temperature (converted from Kelvin to Celsius) is within an optimal range (18-24°C).

Weather Risk to Crops: A flag that identifies "Heavy Rain Risk" (≥ 15mm), "High Wind Risk" (≥ 15 m/s), or "Heat Stress Risk" (average temperature ≥ 25°C).

## 5. Deliverables
A project Report detailing project lifecycle, from data sources to the final analysis.

Data Pipeline: The set of runnable SQL scripts that perform all ETL steps.

Final Power BI Dashboard: The end-user visualization tool that displays the operations, weather, sales, and agricultural advisories based on the generated KPIs.

Executive Summary: A 1-2 page summary of key findings and recommendations.


## 6. Executive Summary
This report details the successful design and implementation of an end-to-end data analytics solution for a Kenya-based e-commerce and produce-delivery startup. The project addresses a critical business need to predict and mitigate risks from adverse weather conditions on delivery operations and agricultural supply chains.

The solution integrates and processes disparate datasets from weather forecasts and internal operational systems. Using a PostgreSQL database, a robust and scalable data model was created to link environmental data with business performance metrics.

Key deliverables of the project include a series of well-documented PostgreSQL scripts that serve as a manual data pipeline, capable of performing all necessary ETL and KPI calculations. This approach was adopted to overcome technical challenges with automated scheduling tools, ensuring the project's core analytical logic is both functional and transparent.

The project successfully generated a suite of actionable KPIs, including:

Delivery Risk Index: A critical tool for the operations team to proactively identify high-risk days and adjust logistics accordingly.

Planting Window Flag: A direct advisory tool for suppliers, helping them make informed decisions based on ideal weather conditions.

Weather Risk to Crops: A metric for suppliers to monitor potential threats to their produce, ensuring stock availability.

By providing these metrics, the project empowers the company to shift from reactive to proactive decision-making. The final deliverables—including the project report, the functional data pipeline scripts, and the planned Power BI dashboard—provide a comprehensive framework to track performance, mitigate risks, and optimize operations and supply chain management.