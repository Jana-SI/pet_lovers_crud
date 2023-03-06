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

    try:
        cursor.execute("insert into cliente (nome, cpf, telefone, numPet) values (%s, %s, %s, %s);",(nome, cpf, telefone, numPet))
        conn.commit()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()
        return (error)   

def inserePet(nome, nascimento, raca, tipo):

    try:
        cursor.execute("insert into pet (nome, nascimento, raca, tipo) values (%s, %s, %s, %s);",(nome, nascimento, raca, tipo))
        conn.commit()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()
        return (error)

def verificaCPFbanco(cpf):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from cliente where cpf=%s;",(cpf, ))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()
        return error

    finally:
        cursor.close()
        conn.close