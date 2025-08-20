from bs4 import BeautifulSoup
import requests
import csv

#url = "https://zucchini.co.ke/collections/vegetables"
url = "https://zucchini.co.ke/"
#requests.get(url)
response = requests.get(url)
#print(response)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
products = soup.find_all('div', class_='wbproductdes card__content')

#with open("products.csv", "w", newline="", encoding="utf-8") as productfile:
with open("products.csv", "w", newline="", encoding="utf-8") as productfile:
    fieldnames = ['Name', 'Price']
    writer = csv.DictWriter(productfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for products in products:
        name_element = products.find('h3', class_='product-title')
        name = name_element.text.strip() if name_element else 'N/A'

        price_element = products.find('span', class_='price-item--sale')
        price = price_element.text.strip() if price_element else 'N/A'

        writer.writerow({'Name': name, 'Price': price})
