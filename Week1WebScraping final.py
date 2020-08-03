import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_url(url):

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    return soup

def scrape_tiki(url="https://tiki.vn/dien-thoai-may-tinh-bang/c1789?_lc=Vk4wMzkwMTAwMDU="):

    soup = get_url(url)

    products = soup.find_all('div', {'class':'product-item'})

    data = []

    # Extract information of each article
    for product in products:
        
        d = {
            'seller_id':'',
            'product_brand':'',
            'product_id':'',
            'product_title':'',
            'price_included_sale':'',
            'image_url':'',
            'sale_percentage':''
        }

        try:
            d['seller_id'] = product['data-seller-product-id']
            d['product_brand'] = product['data-brand']
            d['product_id'] = product['product-sku']
            d['product_title'] = product['data-title']
            d['price_included_sale'] = product['data-price'] 
            d['image_url'] = product.find('span', {'class':'image'}).img['src']

            #check if the price include sale or not
            sale_tag = product.find('span', {'class':'sale-tag sale-tag-square'}).text
            
            if sale_tag:
                d['sale_percentage'] = sale_tag

            #add to product_data array:
            data.append(d)
            
        except:
            # Skip if error and print error message
            pass

    return data

# Scolling to different pages

result = []
from time import sleep
duration = 2

for i in range(10):
    data = scrape_tiki('https://tiki.vn/dien-thoai-may-tinh-bang/c1789?_lc=&page='+str(i))
    result += data
    sleep(duration)
    
# Print out
import pandas as pd

pd.DataFrame(data = result, columns = result[0].keys())