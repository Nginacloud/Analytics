import requests
import csv
cities = {"Nairobi", "Kisumu", "Eldoret", "Nakuru", "Mombasa"}
API_Key = "ce294adfed117d6a54a1b01d507eeef0"


with open("weather_forecasts.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["City", "Time", "Temp (K)", "FeelsLike (K)", "Weather", "Clouds(%)", "Wind(m/s)", "Rain(mm)", "POP"])

    
    for city_name in cities:
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_Key}"
        response= requests.get(url)

        if response.status_code == 200:
            data = response.json()
            forecast = data['list']
            print(data)

            for fcast in forecast:
                writer.writerow([
                    city_name,                                
                    fcast["dt_txt"],
                    fcast["main"]["temp"],
                    fcast["main"]["feels_like"],
                    fcast["weather"][0]["description"],
                    fcast["clouds"]["all"],
                    fcast["wind"]["speed"],
                    fcast.get("rain", {}).get("3h", 0),      
                    fcast["pop"]
                ])