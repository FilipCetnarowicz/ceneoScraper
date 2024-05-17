import requests as re 
from bs4 import BeautifulSoup
id = "99069353"
url = "https://www.ceneo.pl/99069353#tab=reviews_scroll"
#url = "https://www.ceneo.pl/"

http = re.get(url)

print(http.status_code)
#print(http.text)


page = BeautifulSoup(http.text,"html.parser")
# options = page.select
print(page.select_one("div.js_product-reviews"))

page = BeautifulSoup(response.text, "html.parser")
opinions = page.select("div.js_product-review")
opinion = page.select_one("div.js_product-review")
print(type(page))
print(type(opinions))
print(type(opinion))