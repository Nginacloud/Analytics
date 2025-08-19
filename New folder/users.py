import requests
import csv

url = f"https://fakerapi.it/api/v2/users?&_quantity=200&_locale=en_US"

response = requests.get(url)
data = response.json()
print(data)

with open("users.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["id","uuid","firstname","lastname", "username","password","email","ip",
"macAddress","website", "image"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({field: field for field in fieldnames})

    #if 'data' in data:
    for user in data['data']:
        writer.writerow(user)

