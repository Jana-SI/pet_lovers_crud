import psycopg2

host = "localhost"
dbname = "petLovers"
user = "postgres"
password = "1234"
# sslmode = "require"

#inicia conexao
conn_string = "host={0} user={1} dbname={2} password={3}".format(host,user,dbname,password)

conn = psycopg2.connect(conn_string)
print("conexão deu bom")

cursor = conn.cursor()

def insereCliente(nome, cpf, telefone, numPet):
    cursor.execute("insert into cliente (nome, cpf, telefone, numPet) values (%s, %s, %s, %s);",(nome, cpf, telefone, numPet))
    conn.commit()

def inserePet(nome, nascimento, raca, tipo):
    cursor.execute("insert into cliente (nome, nascimento, raca, tipo) values (%s, %s, %s, %s);",(nome, nascimento, raca, tipo))
    conn.commit()

#encerra conexao
# cursor.close()
# conn.close