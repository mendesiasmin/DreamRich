# DreamRich

[![CircleCI](https://circleci.com/gh/DreamRich/DreamRich.svg?style=shield)](https://circleci.com/gh/DreamRich/DreamRich)

[![Build Status](https://travis-ci.org/mendesiasmin/DreamRich.svg?branch=master)](https://travis-ci.org/mendesiasmin/DreamRich)

## Install

``` sh
$ virtualenv v
$ source v/bin/activate
$ pip3 install -r requirements.txt
```

Exporte uma variável de ambiente para indicar qual pasta está o projeto backgend e fronend (**DreamRich e DreamRichJs**).

## Suport scripts

Use um dos seguintes comandos para auxiliar no desenvolvimento.

``` sh
$ $HOME_DREAMRICH/DreamRich/manage.py [ autofix | code_complexity | resetdb | seed -n [NUMBER] | setupdb | stylesheet | test_coverage | test_report ]
```
* autofix: Tenta aplicar pequenas correções na folha de estilo do código python. **Ferramenta:** autopep8;
* code_complexity: exibe métricas do número de linhas e faz análise da complexidade ciclomática do código. **Ferramenta:** radon;
* resetdb: executa as operações de destruir, criar e reaplicar as migrations no banco de dados. **Ferramenta:** django-extensions;
* seed: executa a construção de NUMBER objetos das classes definidas nos arquivos DreamRich[app]/factory.py. **Ferramentas:** factory-boy;
* setup: executa a combinação dos dois comandos anteriores [resetdb + seed]. **Ferramentas:** django-extensions, factory-boy;
* stylesheet: analisa estaticamente o código, exibindo possíveis falhas e erros na folha de estilo de acordo com pep8. **Ferramentas:** pylint;
* test_report: executa os testes unitários e gera um relatório no terminal. **Ferramentas:** coverage;
* test_coverage: executa os testes unitários e gera um relatório que pode ser aberto em html. O comando para abrir é ```$ firefox DreamRich/DreamRich/htmlcov/index.html```. **Ferramentas:** coverage;

## Iniciando servidores


Distribuições Linux com Gnome. (Pode ser utilizado o xterm ou outro terminal de sua preferência)
``` sh
$ gnome-terminal -e "$HOME_DREAMRICH/DreamRich/DreamRich/manage.py runserver" && gnome-terminal -e "npm start --prefix $HOME_DREAMRICH/DreamRichJs/"
```
