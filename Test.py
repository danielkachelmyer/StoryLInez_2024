from bs4 import BeautifulSoup

with open("Index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

tag = doc.title
print(tag.string)
#print(doc)

a_tags = doc.find_all("p")[0]

print(a_tags.find_all("b"))