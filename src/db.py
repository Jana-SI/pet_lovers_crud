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
       
       cursor.execute("insert into pet (nome, nascimento, raca, tipo) values (%s, %s, %s, %s) returning id;",(nome, nascimento, raca, tipo))
       
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

def adicionaNumPet(cpfDono):

    try:
       conn = psycopg2.connect(conn_string)
       cursor = conn.cursor() 
       
       cursor.execute("update cliente set numpet = (numpet+1) where cpf = %s;",(cpfDono, ))
       
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
       
       cursor.execute("insert into donopet (cpfcliente, idpet) values (%s, %s) returning id;",(cpfDono, idPet))
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

        cursor.execute("select * from cliente order by id;")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close


def verificaPetbanco(nome, nascimento, raca, tipo):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from pet where nome=%s and nascimento=%s and raca=%s and tipo=%s;",(nome, nascimento, raca, tipo))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close    

def verificaDonoPetbanco(idPet, cpfcliente):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM pet INNER JOIN donopet ON pet.id = donopet.idpet where pet.id=%s and donopet.cpfcliente = %s;",(idPet, cpfcliente))
        
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisarPets():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from pet order by id;")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def verificaIdPetbanco(idPet):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from pet where id=%s;",(idPet, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisarPetsDonos():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT pet.id, cliente.nome, cliente.telefone, cliente.cpf FROM donopet INNER JOIN pet ON donoPet.idpet = pet.id INNER JOIN cliente ON donoPet.cpfcliente = cliente.cpf")

        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisarPetDonos(idPet):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT pet.id, cliente.nome, cliente.telefone FROM donopet INNER JOIN pet ON donoPet.idpet = pet.id INNER JOIN cliente ON donoPet.cpfcliente = cliente.cpf Where pet.id = %s;",(idPet, ))

        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def deletarCliente(id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("delete from cliente where id=%s returning nome;",(id, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def verificaIdCliente(id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from cliente where id=%s;",(id, ))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def atualizaNomeCliente(nome, id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("update cliente set nome = %s where id = %s",(nome, id))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def atualizaTelefoneCliente(telefone, id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("update cliente set telefone = %s where id = %s returning nome;",(telefone, id))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisaNomeCliente(id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select nome from cliente where id=%s",(id, ))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def desvincularDonoPet(idpet):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("delete from donopet where idpet=%s returning cpfcliente;",(idpet, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def deletarPet(id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("delete from pet where id=%s returning nome;",(id, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def removeNumPet(cpfDono):

    try:
       conn = psycopg2.connect(conn_string)
       cursor = conn.cursor() 
       
       cursor.execute("update cliente set numpet = (numpet-1) where cpf = %s;",(cpfDono, ))
       
       conn.commit()
       return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def desvincularUmDonoPet(idpet, cpf):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("delete from donopet where idpet=%s and cpfcliente=%s;",(idpet, cpf))

        conn.commit()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def atualizaNomePet(nome, id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("update pet set nome = %s where id = %s",(nome, id))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisaNomePet(id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select nome from pet where id=%s",(id, ))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def atualizaTipoRacaPet(tipo, raca, id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("update pet set tipo = %s, raca = %s where id = %s returning nome;",(tipo, raca, id))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def atualizaDataPet(nascimento, id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("update pet set nascimento = %s where id = %s returning nome;",(nascimento, id))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close