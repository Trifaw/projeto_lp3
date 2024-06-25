from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
       {'nome': 'Coca cola', 'descricao': 'Mata sua sede'},
       {'nome': 'Trembolona', 'descricao': 'Você terá um coração gigante'},
       {'nome': 'Red Bull', 'descricao': 'Te dá aasaaaas'},
   ]


app = Flask('Minha App')

# rota + função
# / - home page

@app.route("/servicos")
def servicos ():
    return "<h1>Nossos Serviços<h1>"
    

@app.route('/')
def home ():
    return render_template('home.html')

# /contato - página de contato 
@app.route('/contato')
def contato():
    return render_template('contato.html')

# /produtos - página produtos

@app.route('/produtos')
def produtos():
  
    return render_template('produtos.html', produtos = lista_produtos)

cpf = CPF()

@app.route("/gerar-cpf")
def gerar_cpf():
    
    return f'CPF: {cpf.generate(True)}'

cnpj = CNPJ()

@app.route('/gerar-cnpj')
def gerar_cnpj():

    return f"CNPJ: {cnpj.generate(True)}"

app.run()


# página /serviços retornar "Nossos serviços"
# página /gerar-cpf retornar retornar cpf aleatório
# página /gerar-cnpj retornar cnpj aleatório


# GET /produtos/cadastro devolver form
@app.route('/produtos/cadastro')
def cadastro_produto():
    return render_template('cadastro_produto.html')

# POST /produtos que vai lidar com os dados enviados pelo form
# acessar o objeto request
@app.route('/produtos', methods=['POST'])
def salvar_produto():
    # pegando os valores digitados no form
    # que estão na request
    nome = request.form['nome']
    descricao = request.form['descricao']
    # crio um novo produto (um novo dicionario)
    produto = { 'nome': nome, 'descricao': descricao, 'imagem': ''}
    # adiciona o novo produto na lista
    lista_produtos.append(produto)
    # devolvo o template com o nobo produto
    return render_template('produtos.html', produtos=lista_produtos)
# 
# #
