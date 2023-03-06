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
  numPet = request.form['numPet']

  verificado = verificaCPFbanco(cpfInt)

  if (verificado):
    return jsonify({"cpfValido": "true"})
    
    return render_template('/public/cliente/cadastro_cliente.html', mensagemCadastroSucesso="Cadastrado não realizado, CPF já esta cadastrado no sistema!")

  else:
    return jsonify({"cpfValido": "false"})

    insereCliente(nome, cpfInt, telefone, numPet)

    return render_template('/public/cliente/cadastro_cliente.html', mensagemCadastroSucesso="Cadastrado com sucesso")

@app.route('/cadastro_pet')
def cadastro_pet():
    return render_template('/public/pet/cadastro_pet.html')

@app.route('/cadastro_pet', methods=['GET', 'POST'])
def cadastrarPet():

  nome = request.form['nome']
  nascimento = request.form['nascimento']
  raca = request.form['raca']
  tipo = request.form['tipo']
  
  inserePet(nome, nascimento, raca, tipo)

  return "Cadastro de pet realizado com sucesso!"