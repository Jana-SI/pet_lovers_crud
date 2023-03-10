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

def insereCliente(nome, cpf, telefone):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor() 

        cursor.execute("insert into cliente (nome, cpf, telefone, numPet) values (%s, %s, %s, %s);",(nome, cpf, telefone, 0))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close  

def inserePet(nome, nascimento, raca, tipo):

    try:
       conn = psycopg2.connect(conn_string)
       cursor = conn.cursor() 
       
       cursor.execute("insert into pet (nome, nascimento, raca, tipo) values (%s, %s, %s, %s);",(nome, nascimento, raca, tipo))
       
       conn.commit()
       return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

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

    finally:
        cursor.close()
        conn.close

def adicionaNumPet(idDono):

    try:
       conn = psycopg2.connect(conn_string)
       cursor = conn.cursor() 
       
       cursor.execute("update cliente set numpet = (numpet+1) where id = %s;",(idDono, ))
       
       conn.commit()
       return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def insereDonoPet(cpfDono, idPet):

    try:
       conn = psycopg2.connect(conn_string)
       cursor = conn.cursor() 
       
       cursor.execute("insert into donopet (cpfcliente, idpet) values (%s, %s);",(cpfDono, idPet))
       
       conn.commit()
       return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisarDonos():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from cliente;")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close