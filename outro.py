import mysql.connector

# Função para inserir um novo registro
def inserir_registro(cursor):
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

    print("Novo registro inserido com sucesso!")


# Função para consultar registros
def consultar_registros(cursor):
    # Executando uma consulta para recuperar os registros da tabela
    consulta = "SELECT * FROM employees"
    cursor.execute(consulta)
    registros = cursor.fetchall()

    # Exibindo os registros encontrados
    for registro in registros:
        print(registro)


# Função para atualizar um registro existente
def atualizar_registro(cursor):
    # Solicitando ao usuário para fornecer o ID do registro a ser atualizado
    employee_id = input("Digite o ID do registro a ser atualizado: ")

    # Solicitando ao usuário para inserir os novos valores
    first_name = input("Digite o novo primeiro nome: ")
    last_name = input("Digite o novo sobrenome: ")
    job_id = input("Digite o novo ID do trabalho: ")
    department_id = input("Digite o novo ID do departamento: ")
    salary = float(input("Digite o novo salário: "))

    # Atualizando o registro com os novos valores
    consulta = "UPDATE employees SET first_name = %s, last_name = %s, job_id = %s, department_id = %s, salary = %s WHERE employee_id = %s"
    valores = (first_name, last_name, job_id, department_id, salary, employee_id)

    cursor.execute(consulta, valores)

    # Confirmando a transação
    conexao.commit()

    print("Registro atualizado com sucesso!")


# Função para deletar um registro existente
def deletar_registro(cursor):
    # Solicitando ao usuário para fornecer o ID do registro a ser deletado
    employee_id = input("Digite o ID do registro a ser deletado: ")

    # Deletando o registro com o ID fornecido
    consulta = "DELETE FROM employees WHERE employee_id = %s"
    valores = (employee_id,)

    cursor.execute(consulta, valores)

    # Confirmando a transação
    conexao.commit()

    print("Registro deletado com sucesso!")


# Conectando ao banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='paulo',
    password='senha-aqui',
    database='hr'
)

# Criando um cursor para executar comandos SQL
cursor = conexao.cursor()

# Loop do menu
while True:
    print("----- MENU -----")
    print("1. Inserir registro")
    print("2. Consultar registros")
    print("3. Atualizar registro")
    print("4. Deletar registro")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        inserir_registro(cursor)
    elif opcao == "2":
        consultar_registros(cursor)
    elif opcao == "3":
        atualizar_registro(cursor)
    elif opcao == "4":
        deletar_registro(cursor)
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")

# Fechando a conexão com o banco de dados
cursor.close()
conexao.close()
