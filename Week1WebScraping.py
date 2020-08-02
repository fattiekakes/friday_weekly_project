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

        d = {'seller_id':'','product_id':'','title':'','price':'','image_url':''}

        try:
            d['seller_id'] = product['data-seller-product-id']
            d['product_id'] = product['product-sku']
            d['title'] = product['data-title']
            d['price'] = product['data-price'] 
            d['image_url'] = product.find('span', {'class':'image'}).img['src']


            #add to product_data array:
            data.append(d)
            
        except:
            # Skip if error and print error message
            print("We got one product error!")

    return data

data = scrape_tiki()

import pandas as pd

pd.DataFrame(data = data, columns = data[0].keys())

