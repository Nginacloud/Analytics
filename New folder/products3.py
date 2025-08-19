import requests
import csv

url = f"https://fakerapi.it/api/v2/products?_quantity=200&_locale=en_US&_taxes=12&_categories_type=uuid"

response = requests.get(url)
data = response.json()
print(data)

with open("products3.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["id","name","description","ean", "upc","image","net_price",
"taxes","price"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer.writeheader()
    writer.writerow({field: field for field in fieldnames})

    #if 'data' in data:
    for product in data['data']:
        writer.writerow({
            'id': product['id'],
            'name': product['name'],
            'description': product['description'],
            'ean': product['ean'],
            'upc': product['upc'],
            'image': product['image'],
            'net_price': product['net_price'],
            'taxes': product['taxes'],
            'price': product['price']
        })

