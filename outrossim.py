import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='paulo',
    password='561532palmeira',
    database='hr'
)

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()

# Executando a consulta
consulta = "SELECT salary FROM employees WHERE salary > 5000 AND department_id <> 3"
cursor.execute(consulta)

# Recuperando os resultados da consulta
salarios = cursor.fetchall()

# Exibindo os salários encontrados
for salario in salarios:
    print(salario[0])

# Fechando a conexão com o banco de dados
cursor.close()
conexao.close()
