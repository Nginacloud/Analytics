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

- Handling missing / null values
```python
print(df.isnull().sum())
```
[result](https://github.com/user-attachments/assets/9c718f73-3a4e-4972-bcb7-7f8fec7a88c3)


## Statistical Summary

Descriptive statistics to understand central tendency and spread of data
```python
print(df.describe())
```
![Describe](https://github.com/user-attachments/assets/d4219aa5-79ce-480b-89b4-6d29a6d24610)

```python
correlation_matrix = df.corr()
print(correlation_matrix)
```
![image](https://github.com/user-attachments/assets/1b17d29e-2612-466a-81f1-f16ff0a42179)



## Data visualization
```python
plt.figure(figsize=(14, 7))
df['Wind Speed_km/h'].plot()
plt.title('Wind Speed over Time')
plt.xlabel('Date')
plt.ylabel('Wind Speed km/h')
plt.show()
```
![image](https://github.com/user-attachments/assets/0fbe9648-dc22-401b-ad5f-91e33d299f75)

Correlation
```python
correlation_matrix = df.corr()
plt.figure(figsize=(14, 7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
```
![image](https://github.com/user-attachments/assets/02b1cd55-4028-4160-88c8-14346d69be31)



## Weather patterns and Trends

## Insights and Conclusions

## Recommendations 
