from flask import Flask, request, render_template, redirect,  jsonify
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
  nascimento = request.form['nascimento']
  raca = request.form['raca']
  tipo = request.form['tipo']
  
  inserePet(nome, nascimento, raca, tipo)

  return render_template('/public/cliente/cadastro_pet.html', mensagemCadastroSucesso="Cadastrado do Pet realizado com sucesso")

@app.route('/cadastro_pet_verificando_cpf', methods=['GET', 'POST'])
def verificaDonoPet():

  if request.method == "POST":

    cpf = request.get_json()['cpf'].strip()
    cpfInt = re.sub('[^0-9]', '', cpf)

    verificado = verificaCPFbanco(cpfInt)

  if (verificado):
    return jsonify({"cpfValido": "true"})

  else:
    return jsonify({"cpfValido": "false"})