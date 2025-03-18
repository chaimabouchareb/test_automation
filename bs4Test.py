from bs4 import BeautifulSoup
import requests

url= "http://tutorialsninja.com/demo/"
res = requests.get(url)
doc=BeautifulSoup(res.text,"html.parser")
price = doc.find_all(string="$")

#print(doc.prettify())
"""with open("test.html", "r") as f:
	doc = BeautifulSoup(f, "html.parser")
#print(doc.prettify())
tag = doc.find_all("td")
#print(tag.string)
print(tag)"""
