# Weather Dataset

A brief overview of what the analysis process will look like.

## Table of Contents
- [Installation](#installation)
- [Data overview and Cleaning](#data-overview-and-cleaning)
- [Statistical Summary](#statistical-summary)
- [Data visualization](#data-visualization)
- [Weather patterns and Trends](#weather-patterns-and-trends)
- [Insights and Conclusions](#insights-and-conclusions)
- [Recommendations ](#recommendations)

## Installation

The data is downloaded from kaggle [Here](https://www.kaggle.com/datasets/ayushmi77al/weather-data-set-for-beginners)
Several tools used;
Pandas and numpy
```python
pip install pandas numpy
```

matplotlib and seaborn
```python
pip install matplotlib seaborn
```

## Data overview and Cleaning

- key characteristics of the dataset
```python
df = pd.read_csv(r'C:\Users\USER\OneDrive\Desktop\Project1\1. Weather Data.csv')
print(df)
```

- Handling missing / null values - no null values found
```python
print(df.isnull().sum())
```
![image](https://github.com/user-attachments/assets/3053dd1a-8e5f-46d6-90a0-484841da2a79)


## Statistical Summary

Descriptive statistics to understand central tendency and spread of data
```python
print(df.describe())
```
![image](https://github.com/user-attachments/assets/79be751d-c41a-4acb-af7f-52e46f6b273d)


```python
correlation_matrix = df.corr()
print(correlation_matrix)
```
![image](https://github.com/user-attachments/assets/01153629-8302-4933-8aee-7a82ca01d496)

## Data visualization
```python
plt.figure(figsize=(14, 7))
df['Wind Speed_km/h'].plot()
plt.title('Wind Speed over Time')
plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')
plt.show()
```
![image](https://github.com/user-attachments/assets/d94f0edc-081b-44ca-b86f-7a0270313ab0)


Correlation
```python
correlation_matrix = df.corr()
plt.figure(figsize=(14, 7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```
![image](https://github.com/user-attachments/assets/63546de7-fcfa-4116-b00b-ce4678721bed)


## Weather patterns and Trends
```python
monthly_weather = df.pivot_table(index=df['Date/Time'].dt.month, columns='Weather', aggfunc='size', fill_value=0)
print(monthly_weather)
```

```python
monthly_weather.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Weather Conditions by Month')
plt.xlabel('Month')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.legend(title='Weather Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
```
![image](https://github.com/user-attachments/assets/5cc864f9-a521-4f70-b6e0-3682251be396)

Evident that the weather is mainly clear, and is the consistent condition throughout the year

## Insights and Conclusions

Key Insights;
- The heatmap highlights correlations mostly moderate to weak, which suggests that many of these weather variables maybe independent of each other.
- Temperature increases as Dew point increases, from the strong positive correlation seen
- the wind speed is spread out well throughout the year with defined peaks around January, Feb and March
- Gradual increase in temperature mid-year and very cold (negative celcius) temperature around January
## Recommendations 
- January is cold hence adviced to stay warm
- every month has fair share of extreme conditions so prior preparations like cold-weather outfits is necessary
