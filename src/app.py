from flask import Flask, request, render_template, redirect, jsonify
from src.db import *
from datetime import datetime, time
import re
import holidays
import wtforms

from flask_bootstrap import Bootstrap5
from wtforms import Form, StringField, IntegerField, DateField, SelectField, DateTimeField, ValidationError
from wtforms.validators import Length, InputRequired, DataRequired, Regexp

from flask_babelex import Babel, gettext

app = Flask(__name__)
bootstrap = Bootstrap5(app)
babel = Babel(app)

app.config["PROPAGATE_EXCEPTIONS"] = False

app.config['LANGUAGES'] = {
  'pt': 'Português'
}

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.errorhandler(404) 
def not_found(e): 
  return render_template('/public/erro/error_404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('/public/erro/error_500.html'), 500
              
@app.route('/')
def index():
    return render_template('/public/index.html')

@app.route('/cadastro_cliente')
def cadastro_cliente():
    return render_template('/public/cliente/cadastro_cliente.html')
class CadastroClienteForm(Form):
    nome = StringField('Nome', [InputRequired(), Length(min=6, max=50)])
    cpf = StringField('CPF', [InputRequired(), Length(min=14, max=14)])
    telefone = StringField('Contato', [InputRequired(), Length(min=14, max=15)])

    def validate_nome(self, field):
        if len(field.data) < 6 or len(field.data) > 50:
            raise ValidationError(gettext('O campo Nome deve ter entre 6 e 50 caracteres.'))

@app.route('/cadastro_cliente', methods=['GET', 'POST'])
def cadastrarCliente():

  form = CadastroClienteForm(request.form)

  if form.validate():
      nome = form.nome.data
      cpf = form.cpf.data
      telefone = form.telefone.data
      cpfInt = re.sub('[^0-9]', '', cpf)

      insereCliente(nome, cpfInt, telefone)

      return render_template('/public/cliente/cadastro_cliente.html', sucesso="Cadastrado com sucesso")
  
  else:
    errors = form.errors
    invalid_fields = [field for field, error in errors.items()]
    errorNome = form.errors.get('nome', None)

    if errorNome:
        # Remover os colchetes da mensagem de erro do campo 'nome'
        errorNome = errorNome[0].replace('[', '').replace(']', '')
    
    return render_template('/public/cliente/cadastro_cliente.html', erro="Cadastrado não realizado, tente novamente!", invalid_fields=invalid_fields, errorNome = errorNome)

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
class CadastroPetForm(Form):
    nome = StringField('Nome', [InputRequired(), Length(max=50)])
    tipo = SelectField('Tipo', choices=[('--', '--'), ('ave', 'Ave'), ('cachorro', 'Cachorro'), ('chinchila', 'Chinchila'), ('coelho', 'Coelho'), ('gato', 'Gato'), ('exotico', 'Exótico'), ('hamster', 'Hamster'), ('peixe', 'Peixe'), ('porquinho_da_india', 'Porquinho-da-índia'), ('nao-declarado', 'Não declarado')], validators=[InputRequired()])
    raca = StringField('Raça', validators=[InputRequired(), Length(max=50), Regexp('[a-zA-ZÀ-ÖØ-öø-ÿ]')])
    nascimento = DateField('Nascimento', format='%Y-%m-%d', validators=[InputRequired()])
    donosPet = StringField('CPF do Dono', validators=[InputRequired(), Regexp('\d{3}\.\d{3}\.\d{3}-\d{2}')])

@app.route('/cadastro_pet', methods=['GET', 'POST'])
def cadastrarPet():

  form = CadastroPetForm(request.form)

  if form.validate():
    nome = form.nome.data
    tipo = form.tipo.data
    raca = form.raca.data
    nascimento = form.nascimento.data
    
    cpfDono = form.donosPet.data
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
      
  else:

    donosPet = pesquisarDonos()

    return render_template('/public/pet/cadastro_pet.html', erro="Cadastrado não realizado, tente novamente!", donosPet = donosPet)

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

class AssociarForm(Form):
    idPet = StringField('ID do Pet', validators=[DataRequired(), Length(max=50)])
    donosPet = StringField('CPF do Dono', validators=[DataRequired(), Length(max=14)])

    def validate_donosPet(self, field):
        cpfDono = field.data
        cpfInt = re.sub('[^0-9]', '', cpfDono)

        donoExistente = verificaCPFbanco(cpfInt)

        if not donoExistente:
            raise ValidationError('CPF do dono não encontrado.')
        
    def validate_idPet(self, field):
        idPet = field.data
        
        idPetExistente = verificaIdPetbanco(idPet)

        if not idPetExistente:
            raise ValidationError('Id do pet não encontrado.')

@app.route('/associar_mais_um_dono_pet', methods=['GET', 'POST'])
def associarDonoPet():

  form = AssociarForm(request.form)

  if form.validate():

    idPet = form.idPet.data
    cpfDono = form.donosPet.data
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
    
  else:
    todosPets = pesquisarPets()
    donosPet = pesquisarDonos()
    erroDonosPet = form.errors.get('donosPet', None)
    erroIdPet = form.errors.get('idPet', None)

    if erroDonosPet:
        # Remover os colchetes da mensagem de erro do campo 'donosPet'
        erroDonosPet = erroDonosPet[0].replace('[', '').replace(']', '')

    if erroIdPet:
        # Remover os colchetes da mensagem de erro do campo 'idPet'
        erroIdPet = erroIdPet[0].replace('[', '').replace(']', '')

    return render_template('/public/pet/associar_mais_um_dono.html', erroDonosPet=erroDonosPet, erroIdPet=erroIdPet, todosPets=todosPets, donosPet=donosPet)

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

@app.route('/listar_cliente')
def listar_cliente():

  todosClientes = pesquisarDonos()
  todosClientesOption = pesquisarDonos()
  listarPets = listarPetsCliente()

  return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', todosClientes = todosClientes, todosClientesOption = todosClientesOption, listarPets = listarPets)

@app.route('/listar_cliente_verificando_cpf', methods=['GET', 'POST'])
def verificaCPFListarCliente():

  if request.method == "POST":

    cpf = request.get_json()['cpf'].strip()
    cpfInt = re.sub('[^0-9]', '', cpf)

    verificado = verificaCPFbanco(cpfInt)

  if (verificado):
    return jsonify({"cpfValido": "true"})

  else:
    return jsonify({"cpfValido": "false"})

class ListaClientesForm(Form):
  cliente = StringField('Cliente (CPF)', validators=[DataRequired()])

@app.route('/listar_cliente', methods=['GET', 'POST'])
def CPFListarCliente():

  form = ListaClientesForm(request.form)

  if form.validate():
    cpf = form.cliente.data
    cpfInt = re.sub('[^0-9]', '', cpf)

    clienteEsp = verificaCPFbanco(cpfInt)

    if (clienteEsp):
      
      todosClientesOption = pesquisarDonos()
      listarPets = listarPetsCliente()

      return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', clienteEsp = clienteEsp, todosClientesOption = todosClientesOption, listarPets = listarPets)

    else:
      todosClientes = pesquisarDonos()
      todosClientesOption = pesquisarDonos()
      listarPets = listarPetsCliente()

      return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', todosClientes = todosClientes, todosClientesOption = todosClientesOption, listarPets = listarPets, erro="Cliente não encontrado no sistema, tente novamente!")
  
  else:
    todosClientes = pesquisarDonos()
    todosClientesOption = pesquisarDonos()
    listarPets = listarPetsCliente()

    return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', todosClientes = todosClientes, todosClientesOption = todosClientesOption, listarPets = listarPets, erro="Cliente não encontrado no sistema, tente novamente!")    

@app.route('/listar_cliente_deletar/<idCliente>', methods=['GET', 'POST'])
def deletar_cliente(idCliente):

  todosClientes = pesquisarDonos()
  todosClientesOption = pesquisarDonos()
  listarPets = listarPetsCliente()
  verifica = verificaIdCliente(idCliente)

  if(verifica):

    if(verifica[4] > 0):
      
      erro = "O cliente %s está associado a %s pets e não poderá ser deletado" % (verifica[2],  verifica[4])

      return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', erro = erro, todosClientesOption = todosClientesOption, todosClientes = todosClientes, listarPets = listarPets)

    else:
      nome = deletarCliente(idCliente)
      todosClientes = pesquisarDonos()
      todosClientesOption = pesquisarDonos()
      listarPets = listarPetsCliente()

      sucesso = "O cliente %s foi deletado com sucesso!" % (nome)

      return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', sucesso = sucesso, todosClientesOption = todosClientesOption, todosClientes = todosClientes, listarPets = listarPets)

  else:

    erro = "Não foi possivel deletar, cliente não se encontra no sistema!"

    return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', erro = erro, todosClientesOption = todosClientesOption, todosClientes = todosClientes, listarPets = listarPets)

class AtualizarNomeClienteForm(Form):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=6, max=50)])

@app.route('/listar_cliente_atualizar_nome/<idCliente>', methods=['GET', 'POST'])
def atualizar_cliente_nome(idCliente):

  form = AtualizarNomeClienteForm(request.form)

  if form.validate():

    nome = form.nome.data
    nomeAntigo = pesquisaNomeCliente(idCliente)
    
    atualizaNomeCliente(nome, idCliente)
    
    sucesso = "O nome do cliente %s foi atualizado para %s com sucesso!" % (nomeAntigo[0], nome)

    todosClientes = pesquisarDonos()
    todosClientesOption = pesquisarDonos()
    listarPets = listarPetsCliente()

    return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', sucesso = sucesso, todosClientesOption = todosClientesOption, todosClientes = todosClientes, listarPets = listarPets)

  else:
    erro = "Não foi possivel atualizar o nome do cliente, tente novamente!"

    todosClientes = pesquisarDonos()
    todosClientesOption = pesquisarDonos()
    listarPets = listarPetsCliente()

    return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', erro = erro, todosClientesOption = todosClientesOption, todosClientes = todosClientes, listarPets = listarPets)

class AtualizarTelefoneClienteForm(Form):
    telefone = StringField('Contato', validators=[DataRequired(), Regexp('^\(\d{2}\)\s\d{4,5}-\d{4}$', message='Telefone inválido. Use o formato (00) 00000-0000')])

@app.route('/listar_cliente_atualizar_telefone/<idCliente>', methods=['GET', 'POST'])
def atualizar_cliente_telefone(idCliente):

  form = AtualizarTelefoneClienteForm(request.form)

  if(request.form['telefone']):

    telefone = form.telefone.data

    nome = atualizaTelefoneCliente(telefone, idCliente)
    
    sucesso = "O telefone do cliente %s foi atualizado com sucesso!" % (nome)

    todosClientes = pesquisarDonos()
    todosClientesOption = pesquisarDonos()
    listarPets = listarPetsCliente()

    return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', sucesso = sucesso, todosClientesOption = todosClientesOption, todosClientes = todosClientes, listarPets = listarPets)

  else:
    erro = "Não foi possivel atualizar o telefone do cliente, tente novamente!"

    todosClientes = pesquisarDonos()
    todosClientesOption = pesquisarDonos()
    listarPets = listarPetsCliente()

    return render_template('/public/cliente/listar_deletar_atualizar_clientes.html', erro = erro, todosClientesOption = todosClientesOption, todosClientes = todosClientes, listarPets = listarPets)

@app.route('/listar_pet')
def listar_pet():

  todosPets = pesquisarPets()
  todosPetsOption = pesquisarPets()
  donos = pesquisarPetsDonos()

  return render_template('/public/pet/listar_deletar_atualizar_pets.html', todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)

@app.route('/listar_pet_verificando_id', methods=['GET', 'POST'])
def verificaIdListarPet():

  if request.method == "POST":

    idpet = request.get_json()['idPet'].strip()

    verificado = verificaIdPetbanco(idpet)

  if (verificado):
    return jsonify({"idPetValido": "true"})

  else:
    return jsonify({"idPetValido": "false"})
  
class ListaPetForm(Form):
    idPet = StringField('id do Pet', validators=[DataRequired()])

@app.route('/listar_pet', methods=['GET', 'POST'])
def IDListar_pet():

  form = ListaPetForm(request.form)

  if form.validate():

    idPet = form.idPet.data

    petEsp = verificaIdPetbanco(idPet)

    if(petEsp):

      donosPetEsp = pesquisarPetDonos(idPet)
      todosPetsOption = pesquisarPets()

      return render_template('/public/pet/listar_deletar_atualizar_pets.html', petEsp = petEsp, donosPetEsp = donosPetEsp, todosPetsOption = todosPetsOption)

    else:

      todosPets = pesquisarPets()
      todosPetsOption = pesquisarPets()
      donos = pesquisarPetsDonos()

      return render_template('/public/pet/listar_deletar_atualizar_pets.html', todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption, erro="Pet não encontrado no sistema, tente novamente!")
    
  else:

      todosPets = pesquisarPets()
      todosPetsOption = pesquisarPets()
      donos = pesquisarPetsDonos()

      return render_template('/public/pet/listar_deletar_atualizar_pets.html', todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption, erro="Pet não encontrado no sistema, tente novamente!")


@app.route('/listar_pet_deletar/<idPet>', methods=['GET', 'POST'])
def deletar_pet(idPet):

  verifica = verificaIdPetbanco(idPet)

  if(verifica):

    cpfDonos = desvincularDonoPet(idPet)

    nomePet = deletarPet(idPet)

    if(cpfDonos):
      for cpfDono in cpfDonos:
        removeNumPet(cpfDono)

    sucesso = "O pet %s foi deletado com sucesso!" % (nomePet)

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', sucesso = sucesso, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)

  else:

    erro = "Não foi possivel deletar, o pet não se encontra no sistema!"

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', erros = erro, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)
  
@app.route('/listar_pet_deletar_dono/<idPet>/<cpfDono>', methods=['GET', 'POST'])
def deletar_dono_pet(idPet, cpfDono):

  verifica = verificaIdPetbanco(idPet)

  if(verifica):

    desvincularUmDonoPet(idPet, cpfDono)
    removeNumPet(cpfDono)

    sucesso = "O pet %s foi desassociado ao dono com sucesso!" % (verifica[1])

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', sucesso = sucesso, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)

  else:

    erro = "Não foi possivel desassociar o dono do pet, pet não se encontra no sistema!"

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', erros = erro, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)
class PetAtualizarNomeForm(Form):
    nome = StringField('Nome', validators=[DataRequired(), Length(max=50)])

@app.route('/listar_pet_atualizar_nome/<idPet>', methods=['GET', 'POST'])
def atualizar_pet_nome(idPet):

  form = PetAtualizarNomeForm(request.form)

  if form.validate():

    nome = form.nome.data
    nomeAntigo = pesquisaNomePet(idPet)
    
    atualizaNomePet(nome, idPet)
    
    sucesso = "O nome do pet %s foi atualizado para %s com sucesso!" % (nomeAntigo[0], nome)

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', sucesso = sucesso, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)

  else:
    erro = "Não foi possivel atualizar o nome do pet, tente novamente!"

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', erros = erro, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)
class AtualizarTipoRacaForm(Form):
    tipo = SelectField('Tipo', validators=[DataRequired()], choices=[
        ('', '--'),
        ('ave', 'Ave'),
        ('cachorro', 'Cachorro'),
        ('chinchila', 'Chinchila'),
        ('coelho', 'Coelho'),
        ('gato', 'Gato'),
        ('exotico', 'Exótico'),
        ('hamster', 'Hamster'),
        ('peixe', 'Peixe'),
        ('porquinho_da_india', 'Porquinho-da-índia'),
        ('nao-declarado', 'Não declarado')
    ])
    raca = StringField('Raça', validators=[DataRequired(), Length(max=50), Regexp('[a-zA-ZÀ-ÖØ-öø-ÿ]')])


@app.route('/listar_pet_atualizar_tipo_raca/<idPet>', methods=['GET', 'POST'])
def atualizar_pet_tipo_raca(idPet):

  form = AtualizarTipoRacaForm(request.form)

  if form.validate():

    tipo = form.tipo.data
    raca = form.raca.data
    
    nome = atualizaTipoRacaPet(tipo, raca, idPet)
    
    sucesso = "O tipo e a raça do pet %s foram atualizados com sucesso!" % (nome)

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()
 
    return render_template('/public/pet/listar_deletar_atualizar_pets.html', sucesso = sucesso, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)

  else:
    erro = "Não foi possivel atualizar o tipo e a raça do pet, preencha ambos os campos!"

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', erros = erro, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)
  
class AtualizarDataForm(Form):
    nascimento = DateField('Nascimento', validators=[InputRequired()])

@app.route('/listar_pet_atualizar_data/<idPet>', methods=['GET', 'POST'])
def atualizar_pet_data(idPet):

  form = AtualizarDataForm(request.form)

  if form.validate():

    nascimento = form.nascimento.data
    
    nome = atualizaDataPet(nascimento, idPet)
    
    sucesso = "A data de nascimento do pet %s foi atualiza com sucesso!" % (nome)

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()
 
    return render_template('/public/pet/listar_deletar_atualizar_pets.html', sucesso = sucesso, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)

  else:
    erro = "Não foi possivel atualizar a data de nascimento do pet, preencha os campos!"

    todosPets = pesquisarPets()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/pet/listar_deletar_atualizar_pets.html', erros = erro, todosPets = todosPets, donos = donos, todosPetsOption = todosPetsOption)
  
@app.route('/agendar_consulta')
def agendar_consulta():

  todosPets = pesquisarPets()
  donos = pesquisarPetsDonos()

  return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos)

class AgendarForm(Form):
    idDono = StringField('idDono', validators=[InputRequired()])
    dataHora = DateTimeField('dataHora', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])

@app.route('/agendar_consulta', methods=['GET', 'POST'])
def agendarConsulta():

  form = AgendarForm(request.form)

  if form.validate():
    # obtém os feriados do ano atual no RS, Brasil
    feriados = holidays.Brazil(state='RS')

    idDonoPet = form.idDono.data
    data_hora_str = form.dataHora.data
    data_hora_str = data_hora_str.strftime('%Y-%m-%dT%H:%M')
    data_hora = datetime.strptime(data_hora_str, '%Y-%m-%dT%H:%M')

    todosPets = pesquisarPets()
    donos = pesquisarPetsDonos()
    
    if data_hora in feriados:
      return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, falha = "Data informada é feriado") 

    # Verifica se a data selecionada é um dia útil (segunda a sexta-feira)
    if data_hora.weekday() < 0 or data_hora.weekday() > 4:
      return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, falha = "Data informada não é dia util.")
        # Verifica se o horário selecionado não tem minutos

    if data_hora.minute != 0:
      return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, falha = "Horario inválido, consideramos que cada consulta dura exatemente 1 hora e não aceita minutos alem de H:00.")

    agora_str = datetime.now().strftime('%Y-%m-%dT%H:%M')
    
    if data_hora_str <= agora_str:
      return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, falha = "Horario inválido, agendamento precede o dia e hora deste momento.")

    agendados = listarConsultaData()

    if agendados != None:
      if data_hora in agendados:
        return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, falha = "Horario já ocupado.")

    if time(8, 0) <= data_hora.time() <= time(17, 0):

      agendarConsultaPet(idDonoPet, data_hora)

      return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, sucesso = "Agendamento concluido")
    
    else:
      return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, falha = "Fora de horario de serviço.")
  
  else:
    todosPets = pesquisarPets()
    donos = pesquisarPetsDonos()

    return render_template('/public/consulta/agendar.html', todosPets = todosPets, donos = donos, falha = "Agendamento não realizado, tente novamente!")
    
@app.route('/agendar_consulta_verificando_id', methods=['GET', 'POST'])
def verificaIdagendarConsulta():

  if request.method == "POST":

    idDono = request.get_json()['idDono'].strip()

    verificado = verificaIdDonobanco(idDono)

  if (verificado):
    return jsonify({"idDonoValido": "true"})

  else:
    return jsonify({"idDonoValido": "false"})

@app.route('/listar_consulta')
def listar_consulta():

  consultasHoje = listarConsultaAtual()
  todosPetsOption = pesquisarPets()
  donos = pesquisarPetsDonos()

  if(consultasHoje):
    return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasHoje = consultasHoje)

  else:
    msg = "Não têm consultas hoje!"
    return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, msg=msg)

@app.route('/listar_consulta_futura')
def listar_consulta_futura():

  consultasFuturas = listarConsultaFutura()
  todosPetsOption = pesquisarPets()
  donos = pesquisarPetsDonos()

  if(consultasFuturas):
    return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasFuturas = consultasFuturas)
  
  else:
    msg = "Não têm consultas agendadas!"
    return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, msg=msg)

@app.route('/listar_consulta_historico')
def listar_consulta_passada():

  hitoricoConsultas = listarConsultaPassada()
  todosPetsOption = pesquisarPets()
  donos = pesquisarPetsDonos()

  if(hitoricoConsultas):
    return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, hitoricoConsultas = hitoricoConsultas)
  
  else:
    msg = "Ainda não há historico de consultas!"
    return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, msg=msg)

@app.route('/listar_consulta_deletar/<idConsulta>', methods=['GET', 'POST'])
def deletar_consulta(idConsulta):

  verifica = verificaIdConsulta(idConsulta)

  if(verifica):

    idDono = deletarConsulta(idConsulta)

    dados = pesquisarDadosConsulta(idDono)

    consultasFuturas = listarConsultaFutura()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    if(consultasFuturas):
      return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, dados = dados, consultasFuturas = consultasFuturas)

    else:
      msg = "Não têm consultas agendadas!"
      return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, msg=msg)

  else:

    consultasFuturas = listarConsultaFutura()
    todosPetsOption = pesquisarPets()
    donos = pesquisarPetsDonos()

    erro = "Não foi possivel deletar, a consulta não se encontra no sistema!"

    if(consultasFuturas):
      return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, erro = erro, consultasFuturas = consultasFuturas)
    
    else:
      msg = "Não têm consultas agendadas!"
      return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, erro = erro, msg=msg)
  
class FormAtualizar(Form):
    dataHora = DateTimeField('Data e Hora', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])

@app.route('/listar_consulta_atualizar/<idConsulta>', methods=['GET', 'POST'])
def atualizar_consulta(idConsulta):

  form = FormAtualizar(request.form)

  if form.validate():

    verifica = verificaIdConsulta(idConsulta)

    if(verifica):

      # obtém os feriados do ano atual no RS, Brasil
      feriados = holidays.Brazil(state='RS')
      data_hora_str = form.dataHora.data
      data_hora_str = data_hora_str.strftime('%Y-%m-%dT%H:%M')
      data_hora = datetime.strptime(data_hora_str, '%Y-%m-%dT%H:%M')
      
      consultasFuturas = listarConsultaFutura()
      todosPetsOption = pesquisarPets()
      donos = pesquisarPetsDonos()
      
      if data_hora in feriados:
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasFuturas = consultasFuturas, erro = "Data informada é feriado") 

      # Verifica se a data selecionada é um dia útil (segunda a sexta-feira)
      if data_hora.weekday() < 0 or data_hora.weekday() > 4:
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasFuturas = consultasFuturas, erro = "Data informada não é dia util.")
      
      # Verifica se o horário selecionado não tem minutos
      if data_hora.minute != 0:
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasFuturas = consultasFuturas, erro = "Horario inválido, consideramos que cada consulta dura exatemente 1 hora e não aceita minutos alem de H:00.")

      agora_str = datetime.now().strftime('%Y-%m-%dT%H:%M')
      
      if data_hora_str <= agora_str:
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasFuturas = consultasFuturas, erro = "Horario inválido, agendamento precede o dia e hora deste momento.")

      agendados = listarConsultaData()

      if agendados != None:
        if data_hora in agendados:
          return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasFuturas = consultasFuturas, erro = "Horario já ocupado.")

      if time(8, 0) <= data_hora.time() <= time(17, 0):

        idDono = atualizaConsulta(data_hora, idConsulta)

        dadosAtualiza = pesquisarDadosConsulta(idDono)

        consultasFuturas = listarConsultaFutura()

        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, dadosAtualiza = dadosAtualiza, consultasFuturas = consultasFuturas)
      
      else:
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, consultasFuturas = consultasFuturas, erro = "Fora de horario de serviço.")

    else:

      consultasFuturas = listarConsultaFutura()
      todosPetsOption = pesquisarPets()
      donos = pesquisarPetsDonos()
      
      erro = "Não foi possivel atualizar, a consulta não se encontra no sistema!"

      if(consultasFuturas):
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, erros = erro, donos = donos, consultasFuturas = consultasFuturas)
      
      else:
        msg = "Não têm consultas agendadas!"
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, msg=msg)
  
  else:

      consultasFuturas = listarConsultaFutura()
      todosPetsOption = pesquisarPets()
      donos = pesquisarPetsDonos()
      
      erro = "Não foi possivel atualizar, tente novamente!"

      if(consultasFuturas):
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, erros = erro, donos = donos, consultasFuturas = consultasFuturas)
      
      else:
        msg = "Não têm consultas agendadas!"
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, msg=msg)

class ListarConsultaPetForm(Form):
    idPet = StringField('idPet', validators=[InputRequired()])

@app.route('/listar_consulta', methods=['GET', 'POST'])
def listar_consulta_pet():

  form = ListarConsultaPetForm(request.form)

  if form.validate():
    idPet = form.idPet.data

    petEsp = verificaIdPetbanco(idPet)

    if(petEsp):

      consultaPetEsp = pesquisaConsultaPetESp(idPet)
      donosPetEsp = pesquisarPetDonos(idPet)
      todosPetsOption = pesquisarPets()
      donos = pesquisarPetsDonos()
      
      return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', petEsp = petEsp, donosPetEsp = donosPetEsp, consultaPetEsp = consultaPetEsp, donos = donos, todosPetsOption = todosPetsOption)

    else:
      
      todosPetsOption = pesquisarPets()
      consultasHoje = listarConsultaAtual()
      donos = pesquisarPetsDonos()

      if(consultasHoje):
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', consultasHoje = consultasHoje, todosPetsOption = todosPetsOption, donos = donos, erro="Pet não encontrado no sistema, tente novamente!")
    
      else:
        msg = "Não têm consultas hoje!"
        return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, erro="Pet não encontrado no sistema, tente novamente!", msg=msg)
  
  else:
      
    todosPetsOption = pesquisarPets()
    consultasHoje = listarConsultaAtual()
    donos = pesquisarPetsDonos()

    if(consultasHoje):
      return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', consultasHoje = consultasHoje, todosPetsOption = todosPetsOption, donos = donos, erro="Pet não encontrado no sistema, tente novamente!")
  
    else:
      msg = "Não têm consultas hoje!"
      return render_template('/public/consulta/listar_deletar_atualizar_consulta.html', todosPetsOption = todosPetsOption, donos = donos, erro="Pet não encontrado no sistema, tente novamente!", msg=msg)
  
@app.route('/listar_consulta_pet_verificando_id', methods=['GET', 'POST'])
def verificaIdPetConsulta():

  if request.method == "POST":

    idpet = request.get_json()['idPet'].strip()

    verificado = verificaIdPetbanco(idpet)

  if (verificado):
    return jsonify({"idPetValido": "true"})

  else:
    return jsonify({"idPetValido": "false"})