import requests as req
from bs4 import BeautifulSoup as bs


url = "http://siir.sitesi.web.tr/edip-cansever/"

r = req.get(url)
source = bs(r.content,"html5lib")

solmenu = source.find_all("div",attrs = {"class":"siir"})

linkler = []

for link in solmenu:
  for i in link:
    x = i.get("href")
    linkler.append(x)

for url in linkler:
  new_url = req.get(url)
  new_source = bs(new_url.content,"lxml")
  new_solmenu = new_source.find("div",attrs = {"class":"text"})
  yaz = new_solmenu.text
  with open("siir.txt","a+", encoding = "utf-8") as file:
    file.write(yaz)
