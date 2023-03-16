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
      return render_template('/public/pet/cadastro_pet.html', erro="Cadastro falhou: o pet já se encontra em nosso sistema.")
  else:

    idPet = inserePet(nome, nascimento, raca, tipo)

    petComMesmoDono = verificaDonoPetbanco(idPet, cpfInt)

    if(petComMesmoDono):
        #se usuario se comportar nunca entra neste caso
        return render_template('/public/pet/cadastro_pet.html', erro="Cadastro falhou: o pet já está associado com este dono.")
    else:
    
      adicionaNumPet(cpfInt)
      insereDonoPet(cpfInt, idPet)

      return render_template('/public/pet/cadastro_pet.html', sucesso="Pet cadastrado com sucesso")

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