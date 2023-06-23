# API Flask com Banco de Dados MySQL - README

Este é um guia de instruções para configurar e executar a API Flask com banco de dados MySQL em um contêiner Docker.

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados em seu sistema:

- Python 3.x: https://www.python.org/downloads/
- Flask: Instale o Flask executando o comando `pip install flask` em seu terminal.
- Docker: Siga as instruções de instalação adequadas ao seu sistema operacional disponíveis em: https://www.docker.com/get-started
- Biblioteca de conexão do MySQL em Python: Execute o seguinte comando no terminal para instalá-la:
  ```
  pip install mysql-connector-python
  ```

## Configurando o Banco de Dados MySQL com Docker

1. Certifique-se de ter o Docker instalado em seu sistema. Siga as instruções do link fornecido acima para instalá-lo.

2. Crie um arquivo chamado `docker-compose.yml` e adicione o seguinte conteúdo:

```yaml
version: '3'
services:
  mysql:
    image: mysql:latest
    restart: always
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: NatanSenha
      MYSQL_DATABASE: natanramosferreira
      MYSQL_USER: MyUser
      MYSQL_PASSWORD: NatanSenha
```

Certifique-se de substituir os valores das variáveis de ambiente `MYSQL_ROOT_PASSWORD`, `MYSQL_DATABASE`, `MYSQL_USER` e `MYSQL_PASSWORD` de acordo com suas preferências.

3. Abra o terminal na pasta onde você criou o arquivo `docker-compose.yml` e execute o seguinte comando para iniciar o contêiner do MySQL:

```
docker-compose up -d
```

Isso irá baixar a imagem do MySQL e iniciar o contêiner em segundo plano.

## Configurando e Executando a API Flask

1. Abra um novo arquivo chamado `app.py` e copie o código abaixo para criar a API Flask:

```python
import mysql.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

# Conexão com o banco de dados
mydb = mysql.connector.connect(
    host='localhost',
    user='MyUser',
    password='NatanSenha',
    database='natanramosferreira'
)

# Rotas da API
@app.route('/livros', methods=['GET'])
def consultar_livros():
    # Código da rota consultar_livros()

@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livro_id(id):
    # Código da rota consultar_livro_id(id)

@app.route('/livros', methods=['POST'])
def adicionar_livro():
    # Código da rota adicionar_livro()

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    # Código da rota editar_livro_id(id)

@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    # Código da rota excluir_livro(id)

# Execução da API
if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
```

2. Certifique-se de substituir as informações de conexão do banco de dados (`host`, `user`, `password` e `database`) de acordo com as configurações do seu banco MySQL
