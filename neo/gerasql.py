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
model = "UPDATE filmes SET movie_poster_path = '{}' WHERE id_filme = {};"
sql = ""
ct = 1
for url in urls:
         page = requests.get(url)
         soup = bs4(page.content, "html.parser")
         title = soup.find("div", {"class":"poster"}).a.img["title"]
         imgLink = soup.find("div", {"class":"poster"}).a.img["src"]
         

         title = title.replace(' ', '-')
         title = title.replace(':','-')
         extension = imgLink[-3:]
         name = title+'.'+extension
         path = "filmes/img/"+name
         sql+= model.format(path, ct)
         ct+=1

         
print(sql)

