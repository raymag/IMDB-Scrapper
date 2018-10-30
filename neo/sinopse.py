import csv
from bs4 import BeautifulSoup as bs4
import requests
import urllib

urls = []
try:
         qnt = int(input("Quantos posters deseja baixar? "))
except:
         qnt = 10
with open('movie_metadata.csv', encoding="utf8") as imdb:
         reader  = csv.reader(imdb)
         ct = 0
         for row in reader:
             if row[17] != 'url' and "htt" in row[17]:
                 urls.append(row[17])
             if ct == qnt:
                 break
             ct+=1
print("Processando URLS...")
for url in urls:
         page = requests.get(url)
         soup = bs4(page.content, "html.parser")
         title = soup.find("div", {"class":"poster"}).a.img["title"]
         imgLink = soup.find("div", {"class":"poster"}).a.img["src"]
         sinopse = soup.find("div", {"class":"summary_text"}).get_text()
         print(sinopse)
         print("Baixando poster de", title)
         img = urllib.request.urlretrieve(imgLink, "imagens2/"+title+".jpg")
         print("Poster baixado\n")
print(qnt," poster(s) baixados")

