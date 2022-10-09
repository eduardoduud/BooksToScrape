# BooksToScrape
Projeto de Data Engineering - Webscraping com Python, Selenium e BeautifulSoup, Docked Postgres e Apache Airflow

Sobre o projeto:

- Webscraping realizado utilizando a linguagem Python
- Utilizando a biblioteca Selenium para navegar entre os links das categorias e as páginas.
- Utilizando a biblioteca BeautifulSoup para coletar os dados das páginas HTML.
- Banco de dados Postgres e Apache Airflow rodando em Docker.
- O código gera um arquivo csv e então um script em bash faz a inserção dos dados no banco.
- Gerenciamento desses jobs utilizando o Apache Airflow
- Script de coleta paralelizado. Workers coletam e armazenam os dados dos livros de uma página.
- O script de inserção de dados no banco só roda quando o código python terminar de colear os dados.
