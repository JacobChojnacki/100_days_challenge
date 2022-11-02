import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/Apple-MWP22AM-A-cr-AirPods-Renewed/dp/B0828BJGD2/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0",
    "Accept-Language": "pl,en-US;q=0.7,en;q=0.3"
}

amazon_product = requests.get(URL, headers=header).text

soup = BeautifulSoup(amazon_product, 'lxml')
scrapped_price = soup.select_one("span .a-offscreen").text.replace("$", "")
print(scrapped_price)

if float(scrapped_price) < 120.99:
    # Wyslij email
    pass
