select * from `weather data`;

# set the date/time consistent with current timestamp
update `weather data`
set `Date/Time` = date_format(str_to_date(`Date/Time`, '%Y/%m/%d %H:%i'), '%Y-%m-%d %H:%i');

#1. records where the weather is exactly clear
select * from `weather data`
where Weather = 'clear';

#2. all instances where the weather is clear and the relative humidity is greater than 50, or visibility is above 40.
select * from `weather data`
where (Weather = 'clear'and `Rel Hum_%` > 50) 
or Visibility_km > 40;

#3. the mean value of each column for each weather condition
select Weather,
	round(avg(Temp_C),2) as avg_temperature,
    round(avg(`Dew Point Temp_C`), 2) as avg_dewpoint,
    round(avg(`Rel Hum_%`), 2) as avg_humidity,
    round(avg(`Wind Speed_km/h`), 2) as avg_wind_speed,
    round(avg(Visibility_km), 2) as avg_visibility,
    round(avg(Press_kPa), 2) as avg_pressure
 from `weather data` group by Weather;

#4. number of weather conditions that include snow.
select count(*) from `weather data`
where Weather like '%snow%';