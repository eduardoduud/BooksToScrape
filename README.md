# BooksToScrape
Projeto de Data Engineering - Webscraping com Python, Selenium e BeautifulSoup, Postgres e Apache Airflow, tudo modularizado e paralelizado em Docker

Sobre o projeto:

- Webscraping realizado utilizando a linguagem Python com Docker
- Utilizando a biblioteca Selenium para navegar entre os links das categorias e as páginas.
- Utilizando a biblioteca BeautifulSoup para coletar os dados das páginas HTML.
- O código gera um arquivo .csv e então se conecta no banco e faz a inserção dos dados desse arquivo .csv.
- Banco de dados Postgres e Apache Airflow rodando em Docker.
- [Em desenvolvimento] Gerenciamento dos jobs utilizando o Apache Airflow
- [Em desenvolvimento] Script de coleta paralelizado. Dockers simultâneos coletam e armazenam os dados dos livros de uma página no banco.
