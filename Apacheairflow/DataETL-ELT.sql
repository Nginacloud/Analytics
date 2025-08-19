set search.path = Analytics;

select * from orders1;
select * from products;
select * from users;
select * from weather_forecasts;

alter table products
rename column "Name"  to product_name;

alter table orders1 rename column "id" to user_id;

alter table products
alter column "Price" type INTEGER
using REGEXP_REPLACE("Price", '[^0-9]', '', 'g')::INTEGER;

--alter table weather_forecasts
--alter column "Time" type VARCHAR
--UPDATE weather_forecasts
--SET "Time" = to_char("Time", 'dd/mm/yyyy hh24:mi')::timestamp;

-- This query combines data from all four tables into a single view.

select  
	orders1.order_id,
    orders1.user_id,
    orders1.product_id,
    orders1.city,
    orders1.order_date,
    orders1.delivery_time_minutes,
    orders1.is_cancelled, 
    users.user_id,
    users.fullname,  
    products.product_id,
    products.product_name,
    products."Price",
    --to_char(weather_forecasts."Time", 'dd/mm/yyyy hh24:mi') as weather_datetime,
    weather_forecasts.
    weather_forecasts."Wind(m/s)",
    weather_forecasts."Rain(mm)" ,
    weather_forecasts."Weather"
    --weather_forecasts.
from 
	orders1
inner join 
	users on orders1.user_id = users.user_id
inner join 
	products on orders1.product_id = products.product_id
inner join
    weather_forecasts ON orders1.city = weather_forecasts."City" AND orders1.order_date = weather_forecasts."Time"::DATE;
