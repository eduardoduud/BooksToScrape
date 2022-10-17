# BooksToScrape
Projeto de Data Engineering - Webscraping com Python, Selenium e BeautifulSoup, Postgres e Apache Airflow, tudo modularizado e paralelizado em Docker

Sobre o projeto:

- Webscraping realizado utilizando a linguagem Python com Docker
- Utilizando a biblioteca Selenium para navegar entre os links das categorias e as páginas.
- Utilizando a biblioteca BeautifulSoup para coletar os dados das páginas HTML.
- O código gera um arquivo .csv e então se conecta no banco e faz a inserção dos dados desse arquivo .csv.
- Banco de dados Postgres e Apache Airflow rodando em Docker.
- [Em desenvolvimento] Gerenciamento dos jobs utilizando o Apache Airflow
- [Em desenvolvimento] Orquestração dos containeres utilizando Kubernetes


# Webscraping em Docker

Configuração: Python 3.8, Pandas, Selenium, Bs4, Sqlalchemy, Psycopg2 e latest Chrome Driver

### Buildando a imagem a partir do dockerfile

Dentro da pasta "Docker SeleniumScrape", dê o comando: `docker build . -t "nome"` sendo "nome" o nome que você quer dar pra imagem

# Subindo os containeres do Postgresql e do Airflow

Dentro da pasta "Docker Airflow+Postgre", dê o comando: `docker-compose up -d`

### Acessando o Airflow webserver

Abra seu navegador e acesse `localhost:8080` com o usuário `airflow` e a senha `airflow`

### Acessando o Postgresql

Abra o pgAdmin4 e adicione um banco com o ip `127.0.0.1` e porta `5432`, com o maintenance e username `airflow`

# Executando o webscraping

Dê o comando `docker run -it -rm "nomedaimagem"`, sendo o "nomedaimagem" o nome que você deu ao criar a imagem a partir do dockerfile
