from bs4 import BeautifulSoup
import requests
price=[]
stock=[]
name=[]
desc=[]
result = requests.get("https://electrostar.com.eg/en/product-category/freezers/?number=48&type=list")
page = result.content
soup = BeautifulSoup(page, "html.parser")
item_products = soup.find_all('div', {'class': 'col-md-8 col-sm-8 col-xs-12'})
for product in range(len(item_products)):
    name.append(item_products[product].find('h3', {'class': "title-product"}).text)
    price.append(item_products[product].find('span', {'class': "woocommerce-Price-amount amount"}).text)
    stock.append(item_products[product].find('div', {'class': 'product-stock'}).text.strip())
    desc.append(item_products[product].find('p', {'class': 'product-desc'}).text)
for i in range(len(item_products)):
    print(f'name : {name[i]} \n{stock[i]} \nprice : {price[i]} \ndescription : {desc[i]} \n\n')




