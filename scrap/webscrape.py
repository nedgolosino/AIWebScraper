from bs4 import BeautifulSoup
import requests

# HTML From Website
url = "https://www.jawa.gg/product/28437/powercolor-rx580"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong)