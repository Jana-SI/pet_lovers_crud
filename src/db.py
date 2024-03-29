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

def pesquisarIdDupla():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT donopet.id, cliente.nome, pet.nome, pet.tipo FROM donopet JOIN cliente ON cliente.cpf = donopet.cpfCliente JOIN pet pet ON pet.id = donopet.idPet ORDER BY donopet.id")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def agendarConsultaPet(idDonoPet, dataHora):
    
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor() 

        cursor.execute("insert into consulta (idDonoPet, data) values (%s, %s) RETURNING id;",(idDonoPet, dataHora))

        conn.commit()
        id_consulta = cursor.fetchone()[0]  # Obtém o ID retornado

        return id_consulta

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisarDadosConsultaAgendada(idConsulta):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT c.id, p.nome AS nome_pet, cli.nome AS nome_dono, cast(c.data as time), cast(c.data as date) FROM Consulta c JOIN donoPet dp ON dp.id = c.idDonoPet JOIN pet p ON p.id = dp.idPet JOIN cliente cli ON cli.cpf = dp.cpfCliente WHERE c.id = %s;",(idConsulta, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def verificaIdDonobanco(idDono):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from donopet where id=%s;",(idDono, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def listarConsultaData(dataHora):
    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM consulta WHERE data = %s;", (dataHora,))
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close()

def listarConsultaAtual():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT consulta.id, cast(consulta.data as time), cast(consulta.data as date), cliente.nome, cliente.telefone, pet.nome, pet.tipo, pet.raca, pet.nascimento FROM consulta INNER JOIN donopet on donopet.id = consulta.iddonopet INNER JOIN pet on pet.id = donopet.idpet INNER JOIN cliente ON donopet.cpfcliente = cliente.cpf where consulta.data::date = CURRENT_DATE order by consulta.data")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def listarConsultaFutura():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT consulta.id, cast(consulta.data as time), cast(consulta.data as date), cliente.nome, cliente.telefone, pet.nome, pet.tipo, pet.raca, pet.nascimento FROM consulta INNER JOIN donopet on donopet.id = consulta.iddonopet INNER JOIN pet on pet.id = donopet.idpet INNER JOIN cliente ON donopet.cpfcliente = cliente.cpf where consulta.data::date > CURRENT_DATE order by consulta.data")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def listarConsultaPassada():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT consulta.id, cast(consulta.data as time), cast(consulta.data as date), cliente.nome, cliente.telefone, pet.nome, pet.tipo, pet.raca, pet.nascimento FROM consulta INNER JOIN donopet on donopet.id = consulta.iddonopet INNER JOIN pet on pet.id = donopet.idpet INNER JOIN cliente ON donopet.cpfcliente = cliente.cpf where consulta.data::date < CURRENT_DATE order by consulta.data")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def verificaIdConsulta(idConsulta):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("select * from consulta where id=%s;",(idConsulta, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def deletarConsulta(idConsulta):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("delete from consulta where id=%s returning iddonopet;",(idConsulta, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisarDadosConsulta(idDono):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT cliente.nome, pet.nome FROM donopet INNER JOIN pet on pet.id = donopet.idpet INNER JOIN cliente ON donopet.cpfcliente = cliente.cpf where donopet.id = %s;",(idDono, ))

        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def atualizaConsulta(dataHora, id):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("update consulta set data = %s where id = %s returning iddonopet;",(dataHora, id))
        conn.commit()
        return cursor.fetchone()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def pesquisaConsultaPetESp(idPet):

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT consulta.id, cast(consulta.data as time), cast(consulta.data as date), cliente.nome, cliente.telefone, pet.nome, pet.tipo, pet.raca, pet.nascimento FROM consulta INNER JOIN donopet on donopet.id = consulta.iddonopet INNER JOIN pet on pet.id = donopet.idpet INNER JOIN cliente ON donopet.cpfcliente = cliente.cpf where pet.id = %s;",(idPet, ))
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close

def listarPetsCliente():

    try:
        conn = psycopg2.connect(conn_string)
        cursor = conn.cursor()

        cursor.execute("SELECT cliente.cpf, pet.nome, pet.id, donopet.id FROM cliente JOIN donopet ON cliente.cpf = donopet.cpfcliente JOIN pet ON pet.id = donopet.idpet")
        conn.commit()
        return cursor.fetchall()

    except psycopg2.DatabaseError as error:
        cursor.execute("ROLLBACK")
        conn.commit()

    finally:
        cursor.close()
        conn.close