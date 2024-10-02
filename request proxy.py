import requests

proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "https://10.10.1.10:1080",
}

url = "https://www.amazon.in/s?k=iphone+16&crid=1QDCRB9ZA1SRQ&sprefix=iphon%2Caps%2C428&ref=nb_sb_ss_ts-doa-p_1_5" 
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

soup = requests.get(url , headers=headers)
print(soup.prettify())