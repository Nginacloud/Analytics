### WEATHER DATASET ###
This repository contains python and sql scripts showing EDA of occurences in data manipulation and analysis like counts, filtered records, checking for NULL and mean values.
## OVERVIEW ##
This project demonstrates how to use Python and SQL to perform data analysis on a weather dataset. The script includes the following operations:

1.Reading the csv file
2.Find all records where the weather was exactly clear.

3.Find the number of times the wind speed was exactly 4 km/hr.

4.Check if there are any NULL values present in the dataset.

5.Rename the column "Weather" to "Weather_Condition."

6.What is the mean visibility of the dataset?

7.Find the number of records where the wind speed is greater than 24 km/hr and visibility is equal to 25 km.

8.What is the mean value of each column for each weather condition?

9.Find all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40.

10.Find the number of weather conditions that include snow.

## Data Sources ##
The dataset contains documentation about the weather conditions for the year 2012. The data ranges from Date/Time	Temperature,	Dew Point, Humidity,	Wind Speed in km/h,	Visibility in km	Pressure and Weather conditions.
(Date/Time	Temp_C	Dew Point Temp_C	Rel Hum_%	Wind Speed_km/h	Visibility_km	Press_kPa	Weather)


For the whole set, [Download Here](https://www.kaggle.com/datasets/ayushmi77al/weather-data-set-for-beginners)
## Techniques and tools ##
The project involves basic descriptive analysis to understand the data set and practice various tools like;
- SQL (Dbeaver)
- Python (VScode)
- Power BI
## Explolatory Data Analysis ##
* Must already have pip, python, sql and necessary extentions in vs code already installed
  1. First step
```python
import pandas as pd
```
  2. Import the file from its path
```python
df = pd.read_csv(r'C:\Users\USER\OneDrive\Desktop\Project1\1. Weather Data.csv')
print(df)
```
[8784 rows x 8 columns]

  3. The weather was exactly clear
```python
clear_records = df[df['Weather']=='Clear']
print(clear_records)
```
![alt text](image-1.png)

  4. Speed was exactly 4km/h
```python
count_wind_speed = df[df['Wind Speed_km/h']==4].shape[0]
print(count_wind_speed)
```
Output: 474

  5. If there are Null values
```python
null_values = df.isnull().any().any()
print(null_values)
```
Output: False

  6. Renaming Weather to Weather_Condition
Using inplace impact the original document
```python
df.rename(columns={'Weather': 'Weather_Condition'}, inplace=True)
print(df)
```
  7. Mean visibility (km)
```python
mean_visibility = df['Visibility_km'].mean()
print(mean_visibility)
```
Output: 27.66444672131151
  8. Number of records where wind speed is greater than 24km/h and visibility is 25km
```python
wind_speed_morethan24_visibility_equalto25 = df[(df['Wind Speed_km/h'] > 24) &(df['Visibility_km']==25)].shape[0]
print(wind_speed_morethan24_visibility_equalto25)
```
Output: 308

  9. Mean value of each column for each weather condition
```python
mean_weather_condition = df.groupby('Weather_Condition').mean()
print(mean_weather_condition)
```
![alt text](image-2.png)

  10. instace where weather is clear and relative humidity > 50, or visibility > 40
```python
clear_weather_rel_hum_visibility_filter = df[(df['Weather_Condition']== 'Clear')& (df['Rel Hum_%'] > 50) | (df['Visibility_km']>40)]
print(clear_weather_rel_hum_visibility_filter)
```
![alt text](image-3.png)

  11. Count weather conditions that include snow
```python
snow_condition_count = df[df['Weather_Condition'].str.contains('Snow', case=False)].shape[0]
print(snow_condition_count)
```
Output: 583

