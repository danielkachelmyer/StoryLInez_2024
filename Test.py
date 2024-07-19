from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#print(doc.prettify())

prices = doc.find_all(string="$")
print(prices)

"""
with open("Index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.title
print(tag.string)
#print(doc)

a_tags = doc.find_all("p")[0]

print(a_tags.find_all("b"))
"""