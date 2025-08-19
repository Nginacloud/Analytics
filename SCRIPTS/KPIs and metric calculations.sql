set search_path = Analytics;

select * from orders1;
select * from products;
select * from users;
select * from "Analytics".weather_forecasts;

-- Derived Metric: Daily Rainfall
-- This query calculates the total daily rainfall per city from the weather_forecasts table.

select "City",
	"Time" as forecast_date,
	sum("Rain(mm)") AS total_daily_rainfall_mm
from
	"Analytics".weather_forecasts
group by "City", "Time"
order by "City", forecast_date;

-- Rain Risk Flag (rain ≥ 5 mm or ≥ 3 hours of rain)
-- This query flags a day as "High Risk" if either of the new conditions are met.
select 
    "City",
    "Time" as forecast_date,
    sum("Rain(mm)") as total_daily_rainfall_mm,
    count(case when "Rain(mm)" > 0 then 1 end) as hours_of_rain,
    case
        when sum("Rain(mm)") >= 5 then 'High Rain Risk'
        when count (case when "Rain(mm)" > 0 then 1 end) >= 3 then 'High Rain Risk'
        else 'Low Rain Risk'
    end as rain_risk_flag
from
    "Analytics".weather_forecasts
group by
    "City",
    "Time"
order by
    "City",
    forecast_date;

-- Derived Metric: Wind Risk Flag
-- Similar to the rain risk, this query flags days based on average wind speed.
-- High wind can impact delivery times, especially for light products.
select 
    "City",
    "Time"as forecast_date,
    avg("Wind(m/s)") as avg_daily_wind_ms,
    case
        when avg("Wind(m/s)") > 10 then 'High Wind Risk'
        --when avg("Wind(m/s)") > 5 then 'Medium Wind Risk'
        else 'Medium Wind Risk'
    end as wind_risk_flag
from
    "Analytics".weather_forecasts
group by
    "City",
    "Time"
order by
    "City",
    forecast_date;


-- Derived Metric: Delivery SLA Performance

-- Delivery Risk Index

-- Delivery Risk Index (combined rain/wind risk)
-- This query combines the rain and wind risk flags into a single, comprehensive index.
with daily_risks as (
    -- CTE to get rain and wind risk flags for each day
    select
        "City",
        "Time" as forecast_date,
        case
            when sum("Rain(mm)") >= 5 then 'High'
            when count(case when "Rain(mm)" > 0 then 1 end) >= 3 then 'High'
            else 'Low'
        end as rain_risk,
        case
            when avg("Wind(m/s)") >= 10 then 'High'
            else 'Low'
        end as wind_risk
    from
        "Analytics".weather_forecasts
    group by
        "City",
        "Time"
)
select
    "City",
    forecast_date,
    rain_risk,
    wind_risk,
    case
        when rain_risk = 'High' or wind_risk = 'High' then 'High Delivery Risk'
        else 'Low Delivery Risk'
    end as delivery_risk_index
from
    daily_risks
order by
    --"City",
    forecast_date;

-- Agriculture KPIs
-- 7-Day Cumulative Rainfall (mm)
-- This query uses a window function to calculate the total rainfall over the preceding 7-day period for each city. 
select
    "City",
    "Time" as forecast_date,
    sum("Rain(mm)") over (
        partition by "City"
        order by "Time"
        rows between 6 preceding and current row
    ) as "7_day_cumulative_rainfall_mm"
from
    "Analytics".weather_forecasts
order by
    forecast_date;

-- Planting Window Flag
-- This query identifies potential planting windows based on your criteria:
-- 1. At least 20mm of rain in the last 7 days (to ensure sufficient moisture).
-- 2. heatwave as temperature data.
with seven_day_data as (
    select
        "City",
        "Time" as forecast_date,
        sum("Rain(mm)") over (
            partition by "City"
            order by "Time"
            rows between 6 preceding and current row
        ) as cumulative_rainfall,
        avg("Temp (K)") over (
        partition by "City"
            order by "Time"
            rows between 6 preceding and current row
        )  as avg_temperature
    from
        "Analytics".weather_forecasts
)
select 
    "City",
    forecast_date,
    cumulative_rainfall,
    avg_temperature,
    case
        when cumulative_rainfall >= 20 and avg_temperature >= 289 --and avg_temperature <= 24
        then 'Ideal Planting Window'
        else 'Not an Ideal Planting Window'
    end as "planting_window_flag"
from
    seven_day_data
order by
    "City",
    forecast_date;



-- Weather Risk to Crops
-- This query flags specific weather events that pose a direct risk to crops,
-- such as heavy rain, high wind, or heat stress.
select
    "City",
    "Time" as forecast_date,
    case
        when sum("Rain(mm)") >= 15 then 'Heavy Rain Risk' -- Define "heavy"
        when avg("Wind(m/s)") >= 15 then 'High Wind Risk' -- Define "high"
        when "Weather" in ('hot', 'heatwave') then 'Heat Stress Risk' -- Conceptual
        else 'Low Risk'
    end as "crop_weather_risk"
from
    "Analytics".weather_forecasts
group by
    "City",
    "Time",
    "Weather"
order by
    "City",
    forecast_date;