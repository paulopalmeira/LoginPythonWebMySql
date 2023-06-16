import mysql.connector

# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='paulo',
    password='senha-aqui',
    database='hr'
)

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()

# Obtendo o último employee_id existente
cursor.execute("SELECT MAX(employee_id) FROM employees")
ultimo_id = cursor.fetchone()[0]

# Verificando se há registros existentes na tabela
if ultimo_id is None:
    novo_id = 1
else:
    novo_id = ultimo_id + 1

# Solicitando ao usuário para inserir os valores
first_name = input("Primeiro nome: ")
last_name = input("Sobrenome: ")
job_id = input("ID do trabalho: ")
department_id = input("ID do departamento: ")
salary = float(input("Digite o salário: "))

# Inserindo um novo registro com o novo_id
consulta = "INSERT INTO employees (employee_id, first_name, last_name, job_id, department_id, salary) VALUES (%s, %s, %s, %s, %s, %s)"
valores = (novo_id, first_name, last_name, job_id, department_id, salary)

cursor.execute(consulta, valores)

# Confirmando a transação
conexao.commit()

# Fechando a conexão com o banco de dados
cursor.close()
conexao.close()