# Gerência e Configuração de Software

Iasmin Mendes, 14/0041940

Este projeto visa implementar componentes de Gerência e Configuração de Software no projeto [DreamRich](https://github.com/DremRich/DreamRich).

##### Docker

1. docker-compose build
1. docker-compose up

###### Comandos para rodar construir o banco de dados

1. docker run dreamrich_api python3 manage.py reset_db
1. docker run dreamrich_api python3 manage.py make_db
1. docker run dreamrich_api python3 manage.py load_db
1. docker run dreamrich_api python3 manage.py load_all

