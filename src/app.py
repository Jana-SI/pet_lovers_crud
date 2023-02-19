from flask import Flask, request, render_template, redirect
from src.db import *

app = Flask(__name__)

@app.errorhandler(404) 
def not_found(e): 
  return render_template('/public/404.html')
              
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