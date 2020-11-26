from bs4 import BeautifulSoup

import requests

html = requests.get("https://www.cptec.inpe.br/sp/guaratingueta").content

soup = BeautifulSoup(html, 'html.parser')

#print(soup.prettify())

temperaturaMaxima = soup.find("div", class_="bloco-previsao d-flex flex-column text-center").find("label")

print(temperaturaMaxima.string)