from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import false

options = Options()
options.add_argument("--window-size=1400,900")
navegador = webdriver.Chrome(chrome_options=options)

navegador.get("http://books.toscrape.com/")

page_content = navegador.page_source

site = BeautifulSoup(page_content, "html.parser")

dadoslivros=[]

livros = site.findAll('li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
i=0
while(i<49):
    for livro in livros:
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, "html.parser")
        livros = site.findAll('li', attrs={'class': 'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        
        nome = livro.find('h3').text
        preco = livro.find('p', attrs={'class': 'price_color'}).text
        estoque = livro.find('p', attrs={'class': 'instock availability'}).text.strip()
        nota=0
        if(livro.find('p', attrs={'class': 'star-rating One'})):
            nota = +1
        if(livro.find('p', attrs={'class': 'star-rating Two'})):
            nota = +2
        if(livro.find('p', attrs={'class': 'star-rating Three'})):
            nota = +3
        if(livro.find('p', attrs={'class': 'star-rating Four'})):
            nota = +4
        if(livro.find('p', attrs={'class': 'star-rating Five'})):
            nota = +5
            
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print(nome)
        print(preco)
        print(nota)
        print(estoque)
        dadoslivros.append([nome, preco, nota, estoque])
    i= i+1
    print(i)
    next = navegador.find_element(By.CLASS_NAME, 'next a').click()
dados = pd.DataFrame(dadoslivros, columns=['Nome', 'Preço', 'Nota', 'Estoque'])
dados.to_csv('dadoslivros.csv', index=false)
