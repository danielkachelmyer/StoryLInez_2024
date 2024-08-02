import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin
import json
import os

def get_soup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        return None

def extract_images(soup, base_url):
    images = []
    for idx, img_tag in enumerate(soup.find_all('img', {'src': re.compile('.jpg')})):
        img_url = img_tag.get('src')
        if img_url and not img_url.startswith('data:'):
            full_url = urljoin(base_url, img_url)
            images.append(full_url)
            download_image(full_url, f'image_{idx+1}.jpg')
    return images

def extract_colors(soup):
    colors = []
    for div in soup.find_all('div', style=re.compile('background-color:')):
        style = div.get('style')
        color = re.findall(r'background-color:\s*([^;]+)', style)
        if color:
            colors.append(color[0])
    return colors

def extract_ad_copy(soup):
    ad_copy = []
    for p_tag in soup.find_all('p'):
        ad_copy.append(p_tag.get_text().strip())
    return ad_copy

def extract_offers(soup):
    offers = []
    for div in soup.find_all(['div', 'span'], class_=re.compile('offer|promo|discount')):
        offers.append(div.get_text().strip())
    return offers

def extract_pricing(soup):
    pricing = []
    for span in soup.find_all(['span', 'div'], class_=re.compile('price|pricing|amount')):
        pricing.append(span.get_text().strip())
    return pricing

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)

def main():
    url = input("Enter the URL of the website: ")
    soup = get_soup(url)
    
    if soup:
        data = {
            "images": extract_images(soup, url),
            "colors": extract_colors(soup),
            "ad_copy": extract_ad_copy(soup),
            "offers": extract_offers(soup),
            "pricing": extract_pricing(soup)
        }

        with open('output.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

        # Display the output in the terminal
        print("\nImages:")
        for img in data["images"]:
            print(img)
        
        print("\nColors:")
        for color in data["colors"]:
            print(color)
        
        print("\nAd Copy:")
        for ad in data["ad_copy"]:
            print(ad)
        
        print("\nOffers:")
        for offer in data["offers"]:
            print(offer)
        
        print("\nPricing:")
        for price in data["pricing"]:
            print(price)
        
        print("\nData has been successfully extracted and saved to output.json.")
    else:
        print("Failed to retrieve the website.")

if __name__ == "__main__":
    main()

#https://hisglory.shop/collections/all
