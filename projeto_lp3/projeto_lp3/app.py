from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

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
    lista_produtos = [
        {'nome': 'Coca cola', 'descricao': 'Mata sua sede'},
        {'nome': 'Trembolona', 'descricao': 'Você terá um coração gigante'},
        {'nome': 'Red Bull', 'descricao': 'Te dá aasaaaas'},
    ]

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
