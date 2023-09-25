import mysql.connector
from mysql.connector import errorcode

print("Conectando...")

try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='K@yque5655'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS LOGIN;")

cursor.execute("CREATE DATABASE LOGIN;")

cursor.execute("USE LOGIN;")

# criando tabelas
TABLES = {}
TABLES['Usuarios'] = ('''
      CREATE TABLE usuarios (
      email VARCHAR(255) PRIMARY KEY,
      nome VARCHAR(255) not null,
      senha VARCHAR(255) not null
)''')


for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print(f'Criando tabela {tabela_nome}:', end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()