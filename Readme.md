# Projeto de Desenvolvimento de Sistemas Orientados a Objetos I :file_folder:
---
### Infos :clipboard:

Projeto desenvolvido para a aula da Projeto de Desenvolvimento de Sistemas Orientados a Objetos I, UFSC, ministrado pelos professores, Jean Hauck e Thais Bardini Idalino, projeto desenvolvido pelos alunos, Israel Schmitt Joaquim e Lissandro Roberto Wilford Arabia Rezende.

---
### Infra :open_file_folder:

Arquitetura de três camadas, tentando seguir o padrão [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), com uso da biblioteca [flask](https://flask.palletsprojects.com/en/2.0.x/) para um servidor web.

```
project
├── Dockerfile
├── config.py
├── app.py
├── requirements.txt
└── src
    ├── __init__.py
    ├── controllers
    |   ├── __init__.py
    │   └── ...
    │
    ├── models
    |   ├── __init__.py
    │   └── ...
    │
    ├── routes
    |   ├── __init__.py
    │   └── ...
    |
    └── views
        ├── __init__.py
        └── ...
```
---
### Camada de apresentação (view)

A camada de apresentação será responsável por receber as chamadas e encaminhar para a camada de serviços.

Esta camada também vai ser responsável por receber as respostas da camada de serviço e apresentar para o usuário em forma de JSON ou qualquer outro content type.

Além disso, todos os erros que vierem das camadas inferiores, sejam eles relativos ou não à camada de apresentação, serão tratados e exibidos pelo usuário nesta mesma camada.

---
### Camada de Serviço (controller)

A camada de serviço será responsável por fazer a comunicação com todo o resto da arquitetura. Cada serviço receberá pelo menos uma instancia de um repositório da camada de dados, podendo receber também outros serviços.

---
### Camada de dados (models)

A camada de dados é a responsável pela comunicação com fontes externas de dados (APIs, DBs).

#### Conexões

Nesta camada que será um agregado de conexões de bancos de dados que podem ser utilizadas.

Aqui estarão os arquivos que gerarão e conectarão com os bancos de dados, mas não vão realizar nenhum tipo de operação.

#### Repositórios

Os repositórios serão os manipuladores dos clientes de bancos de dados. Serão eles que vão realizar as operações no banco de dados e retornar os dados propriamente ditos.