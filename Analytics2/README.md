# Weather Dataset

A brief overview of what the analysis process will look like.

## Table of Contents
- [Installation](#installation)
- [Data Overview and Cleaning](dataoverviewandcleaning)
- [Statistical Summary](statisticalsummary)
- [Data visualization](data_visualization)
- [Weather patterns and Trends](weatherpatternsandtrends)
- [Insights and Conclusions](insightsandconclusions)
- [Recommendations ](recommendations)

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
![alt text](image-5.png)


## Statistical Summary

Descriptive statistics to understand central tendency and spread of data
```python
print(df.describe())
```
![alt text](image-4.png)

```python
correlation_matrix = df.corr()
print(correlation_matrix)
```
![alt text](image-3.png)



## Data visualization
```python
plt.figure(figsize=(14, 7))
df['Wind Speed_km/h'].plot()
plt.title('Wind Speed over Time')
plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')
plt.show()
```
![alt text](image-2.png)


Correlation
```python
correlation_matrix = df.corr()
plt.figure(figsize=(14, 7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```
![alt text](image-1.png)



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
![alt text](image.png)

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
