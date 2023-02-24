from flask import Flask, request, render_template, redirect
from src.db import *
from flask_bootstrap import Bootstrap5

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
  telefone = request.form['telefone']
  numPet = request.form['numPet']

  insereCliente(nome, cpf, telefone, numPet)

  return "Cadastro realizado com sucesso!"

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