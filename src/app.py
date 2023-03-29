from flask import Flask, request, render_template, redirect, jsonify
from src.db import *
from flask_bootstrap import Bootstrap5
import re

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.errorhandler(404) 
def not_found(e): 
  return render_template('/public/error_404.html')
              
@app.route('/')
def index():
    return render_template('/public/index.html')

@app.route('/cadastro_cliente')
def cadastro_cliente():
    return render_template('/public/cliente/cadastro_cliente.html')

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastrarCliente():

  nome = request.form['nome']
  cpf = request.form['cpf']
  cpfInt = re.sub('[^0-9]', '', cpf)

  telefone = request.form['telefone']

  insereCliente(nome, cpfInt, telefone)

  return render_template('/public/cliente/cadastro_cliente.html', mensagemCadastroSucesso="Cadastrado com sucesso")

@app.route('/cadastro_cliente_verificando_cpf', methods=['GET', 'POST'])
def verificaCPF():

  if request.method == "POST":

    cpf = request.get_json()['cpf'].strip()
    cpfInt = re.sub('[^0-9]', '', cpf)

    verificado = verificaCPFbanco(cpfInt)

  if (verificado):
    return jsonify({"cpfValido": "true"})

  else:
    return jsonify({"cpfValido": "false"})

@app.route('/cadastro_pet')
def cadastro_pet():

  donosPet = pesquisarDonos()

  return render_template('/public/pet/cadastro_pet.html', donosPet = donosPet)

@app.route('/cadastro_pet', methods=['GET', 'POST'])
def cadastrarPet():

  nome = request.form['nome']
  tipo = request.form['tipo']
  raca = request.form['raca']
  nascimento = request.form['nascimento']
  
  cpfDono = request.form['donosPet']
  cpfInt = re.sub('[^0-9]', '', cpfDono)
  
  petJaExiste = verificaPetbanco(nome, nascimento, raca, tipo)
  
  if(petJaExiste):
    donosPet = pesquisarDonos()

    return render_template('/public/pet/cadastro_pet.html', erro="Cadastro falhou: o pet já se encontra em nosso sistema.", donosPet = donosPet)
  else:

    donosPet = pesquisarDonos()

    idPet = inserePet(nome, nascimento, raca, tipo)

    petComMesmoDono = verificaDonoPetbanco(idPet, cpfInt)

    if(petComMesmoDono):

      return render_template('/public/pet/cadastro_pet.html', erro="Cadastro falhou: o pet já está associado com este dono.", donosPet = donosPet)

    else:
    
      adicionaNumPet(cpfInt)
      insereDonoPet(cpfInt, idPet)

      return render_template('/public/pet/cadastro_pet.html', sucesso="Pet cadastrado com sucesso", donosPet = donosPet)

@app.route('/cadastro_pet_verificando_cpf', methods=['GET', 'POST'])
def verificaCPFcadPet():

  if request.method == "POST":

    cpf = request.get_json()['cpf'].strip()
    cpfInt = re.sub('[^0-9]', '', cpf)

    verificado = verificaCPFbanco(cpfInt)

  if (verificado):
    return jsonify({"cpfValido": "true"})

  else:
    return jsonify({"cpfValido": "false"})

@app.route('/associar_mais_um_dono_pet')
def associar_mais_um_dono_pet():

  todosPets = pesquisarPets()
  donosPet = pesquisarDonos()

  return render_template('/public/pet/associar_mais_um_dono.html', todosPets = todosPets, donosPet = donosPet)

@app.route('/associar_mais_um_dono_pet', methods=['GET', 'POST'])
def associarDonoPet():

  idPet = request.form['idPet']
  
  cpfDono = request.form['donosPet']
  cpfInt = re.sub('[^0-9]', '', cpfDono)

  petComMesmoDono = verificaDonoPetbanco(idPet, cpfInt)

  if(petComMesmoDono):

    todosPets = pesquisarPets()
    donosPet = pesquisarDonos()
    
    return render_template('/public/pet/associar_mais_um_dono.html', erro="Cadastro falhou: o pet já está associado com este dono.", todosPets = todosPets, donosPet = donosPet)

  else:
  
    todosPets = pesquisarPets()
    donosPet = pesquisarDonos()
  
    adicionaNumPet(cpfInt)
    insereDonoPet(cpfInt, idPet)

    return render_template('/public/pet/associar_mais_um_dono.html', sucesso="Pet associado ao dono com sucesso", todosPets = todosPets, donosPet = donosPet)

@app.route('/associar_mais_um_dono_pet_verificando_cpf', methods=['GET', 'POST'])
def verificaCPFassociaPet():

  if request.method == "POST":

    cpf = request.get_json()['cpf'].strip()
    cpfInt = re.sub('[^0-9]', '', cpf)

    verificado = verificaCPFbanco(cpfInt)

  if (verificado):
    return jsonify({"cpfValido": "true"})

  else:
    return jsonify({"cpfValido": "false"})

@app.route('/associar_mais_um_dono_pet_verificando_id', methods=['GET', 'POST'])
def verificaIdAssociaPet():

  if request.method == "POST":

    idpet = request.get_json()['idPet'].strip()

    verificado = verificaIdPetbanco(idpet)

  if (verificado):
    return jsonify({"idPetValido": "true"})

  else:
    return jsonify({"idPetValido": "false"})

@app.route('/consultar_cliente')
def consultar_cliente():

  todosClientes = pesquisarDonos()
  todosClientesOption = pesquisarDonos()

  return render_template('/public/cliente/consultar_clientes.html', todosClientes = todosClientes, todosClientesOption = todosClientesOption)

@app.route('/consultar_cliente_verificando_cpf', methods=['GET', 'POST'])
def verificaCPFconsultarCliente():

  if request.method == "POST":

    cpf = request.get_json()['cpf'].strip()
    cpfInt = re.sub('[^0-9]', '', cpf)

    verificado = verificaCPFbanco(cpfInt)

  if (verificado):
    return jsonify({"cpfValido": "true"})

  else:
    return jsonify({"cpfValido": "false"})

@app.route('/consultar_cliente', methods=['GET', 'POST'])
def CPFconsultarCliente():

  cpf = request.form['cliente']
  cpfInt = re.sub('[^0-9]', '', cpf)

  clienteEsp = verificaCPFbanco(cpfInt)

  if (clienteEsp):
    
    todosClientesOption = pesquisarDonos()

    return render_template('/public/cliente/consultar_clientes.html', clienteEsp = clienteEsp, todosClientesOption = todosClientesOption)

  else:
    todosClientes = pesquisarDonos()
    todosClientesOption = pesquisarDonos()

    return render_template('/public/cliente/consultar_clientes.html', todosClientes = todosClientes, todosClientesOption = todosClientesOption, erro="Cliente não encontrado no sistema, tente novamente!")

@app.route('/consultar_pet')
def consultar_pet():

  todosPets = pesquisarPets()
  todosPetsOption = pesquisarPets()
  donos = pesquisarPetsDonos()

  return render_template('/public/pet/consultar_pets.html', todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)

@app.route('/consultar_pet_verificando_id', methods=['GET', 'POST'])
def verificaIdConsultarPet():

  if request.method == "POST":

    idpet = request.get_json()['idPet'].strip()

    verificado = verificaIdPetbanco(idpet)

  if (verificado):
    return jsonify({"idPetValido": "true"})

  else:
    return jsonify({"idPetValido": "false"})

@app.route('/consultar_pet', methods=['GET', 'POST'])
def IDconsultar_pet():

  idPet = request.form['idPet']

  petEsp = verificaIdPetbanco(idPet)

  if(petEsp):

    donosPetEsp = pesquisarPetDonos(idPet)
    todosPetsOption = pesquisarPets()

    return render_template('/public/pet/consultar_pets.html', petEsp = petEsp, donosPetEsp = donosPetEsp, todosPetsOption = todosPetsOption)

  else:

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/consultar_pets.html', todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption, erro="Pet não encontrado no sistema, tente novamente!")