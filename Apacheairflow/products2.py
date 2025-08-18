from bs4 import BeautifulSoup
import requests
import csv

url = "https://naivas.online/"

#requests.get(url)
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
products = soup.find_all('div', class_='h-full')
if not products:
    print("No product containers found. Check the class name.")
    exit()
with open("product.csv", "w", newline="", encoding="utf-8") as productfile:
    fieldnames = ['Name', 'Price']
    writer = csv.DictWriter(productfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for products in products:
        name_element = products.find('a', class_='!text-naivas-gray-dark')
        name = name_element.text.strip() if name_element else 'N/A'

        price_element = products.find('span', class_='font-bold text-naivas-green')
        price = price_element.text.strip() if price_element else 'N/A'

        writer.writerow({'Name': name, 'Price': price})
