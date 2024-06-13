from flask import Flask
from validate_docbr import CPF, CNPJ

app = Flask('Minha App')

# rota + função
# / - home page

@app.route("/servicos")
def servicos ():
    return "<h1>Nossos Serviços<h1>"
    

@app.route('/')
def home ():
    return '<h1>Home Page</h1>'

# /contato - página de contato 
@app.route('/contato')
def contato():
    return "<h1>Contato</h1>"

# /produtos - página produtos

@app.route('/produtos')
def produtos():
    return '<h1>Produtos</h1>'

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
