# import requests
# from bs4 import BeautifulSoup

# proxies = {
#   "http": "http://10.10.1.10:3128",
#   "https": "https://10.10.1.10:1080",
# }

# url = "https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q=iphone" 
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# r = requests.get(url , headers=headers)

# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
# divs = soup.find(class_ = "app-stores")
# print(divs)

from bs4 import BeautifulSoup
import requests
import pandas as pd
