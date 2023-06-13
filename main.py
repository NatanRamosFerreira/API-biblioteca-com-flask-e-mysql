import mysql.connector
from flask import Flask, jsonify, request

'''
Objetivos dessa API:
    1-feita para exercitar as nocoes basicas sobre APi e a importancia desse conhecimento
    2-Depois de pronta quero implementar o acesso ao banco de dados
'''

#conexao com o banco de dados
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'MyUser',
    password = 'NatanSenha',
    database = 'natanramosferreira'
    )


app = Flask(__name__)

# Colsutar todos os livros
'''
Coleta todos os dados do Bd(ainda em WardCode)
'''
@app.route('/livros', methods = ['GET'])
def consultar_livros():
    meu_cursor = mydb.cursor()
    query = meu_cursor.execute('SELECT * FROM livros')
    todos_os_livros = meu_cursor.fetchall()

    livros = list()
    for livro in todos_os_livros:
        livros.append(
            {
            'id': livro[0],
            'titulo': livro[1],
            'autor': livro[2]
            }
        )

    return jsonify(
        mensagem = 'lista de livros',
        dados = livros
    )

#consultar Livro por id
'''
otimização do metodo de busca , 
saindo de uma lista para um dicionario para a busca ser unica
'''
# Consultar Livro por id
@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livro_id(id):
    cursor = mydb.cursor()
    query = "SELECT * FROM livros WHERE id = %s"
    cursor.execute(query, (id,))
    livro = cursor.fetchone()
    cursor.close()

    if livro is None:
        return jsonify({'mensagem': 'Livro não encontrado'})

    livro_selecionado = {
        'id': livro[0],
        'titulo': livro[1],
        'autor': livro[2]
    }

    return jsonify(livro_selecionado)
# Adicionar Livro
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    cursor = mydb.cursor()

    query = "INSERT INTO livros (id, titulo, autor) VALUES (%s, %s, %s)"
    livro_data = (novo_livro['id'], novo_livro['titulo'], novo_livro['autor'])
    cursor.execute(query, livro_data)
    mydb.commit()

    cursor.close()

    return jsonify(novo_livro)

@app.route('/livros/<int:id>', methods=['PUT'])
def editar_livro_id(id):
    alterar_livro = request.get_json()
    cursor = mydb.cursor()

    query = "UPDATE livros SET titulo = %s, autor = %s WHERE id = %s"
    dados_livro = (alterar_livro['titulo'], alterar_livro['autor'], id)
    cursor.execute(query, dados_livro)
    mydb.commit()

    cursor.close()

    return jsonify(alterar_livro)

# Excluir Livro 
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    cursor = mydb.cursor()

    '''
    Verificar se o livro existe antes de excluir
    OBS: É preciso transformar esse consulta em um modulo
    para nao precisar escrever tudo novamente  e o codigo
    ficar mais modularizado.
    '''
    query = "SELECT * FROM livros WHERE id = %s"
    livro_id = (id,)
    cursor.execute(query, livro_id)
    livro = cursor.fetchone()

    if livro is None:
        cursor.close()
        return jsonify({'mensagem': 'Livro não encontrado'})

    # Excluir o livro
    query = "DELETE FROM livros WHERE id = %s"
    cursor.execute(query, livro_id)
    mydb.commit()

    cursor.close()

    return jsonify({'mensagem': 'Livro excluído'})


        
#Definindo aonde vai rodar a API
app.run(port=5000, host = 'localhost', debug = True)
