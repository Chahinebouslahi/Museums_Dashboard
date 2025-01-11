from bs4 import BeautifulSoup
import os
import requests
import xlsxwriter
import pandas as pd

doc=requests.get("https://fr.wikipedia.org/wiki/Liste_des_mus%C3%A9es_d%27art_les_plus_visit%C3%A9s_au_monde")
page=doc.content
#recupération du contenu HTML
scrap=BeautifulSoup(page,'lxml')
museums=[]
#recherche des informations
tab=scrap.find('table',{'class': 'wikitable'})
rows=tab.find_all('tr')
for row in rows[1:]:
    info = row.find_all('td')
    rank = info[0].text.strip()
    name=info[1].text.strip() 
    city=info[2].text.strip()
    country=info[3].text.strip()
    nbvisitors=info[4].text.strip()
    #ajout des informations
    museums.append({'rank':rank,
                  'Musée':name,
                  'Ville':city,
                  'Pays':country,
                  'Nombre de visiteurs':nbvisitors
                  })  
df = pd.DataFrame(museums)
#to Excel
df.to_excel('museum.xlsx',index=False)

print("Données exportées avec succès dans 'musees_plus_visites.xlsx'")
