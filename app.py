from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuração da conexão com o banco de dados MySQL
db_config = {
    'host': 'localhost',
    'user': 'paulo',
    'password': '---',
    'database': 'sistemao',
}

# Função para realizar a inserção dos dados do formulário no banco de dados
def inserir_dados(usuario, senha, email, nome_completo):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Executa a inserção dos dados na tabela logadores
    query = "INSERT INTO logadores (usuario, senha, email, nome_completo) VALUES (%s, %s, %s, %s)"
    values = (usuario, senha, email, nome_completo)
    cursor.execute(query, values)

    # Confirma as alterações no banco de dados
    conn.commit()

    # Fecha a conexão com o banco de dados
    cursor.close()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # Obter os dados do formulário de cadastro
        usuario = request.form['usuario']
        senha = request.form['senha']
        email = request.form['email']
        nome_completo = request.form['nome_completo']

        # Chama a função para inserir os dados no banco de dados
        inserir_dados(usuario, senha, email, nome_completo)

        # Redirecionar para uma página de confirmação ou exibir uma mensagem de sucesso
        return render_template('confirmacao.html')

    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run()
