# pip3 install flask
from flask import  Flask
from calc import soma, subtracao, divisao, multiplicacao

app = Flask(__name__)

h1 = '<h1>Calculadora...</h1>'

@app.route('/')

def index():
  h1 = '<h1>Calculadora Olist</h1>'
  ol = '''
          <ol>
            <li><a href="/soma">Somar</a></li>
            <li><a href="/subtracao">Subtrair</a></li>
            <li><a href="/divisao">Divisão</a></li>
            <li><a href="/multiplicar">Multiplicar</a></li>          
          </ol>  
       '''
  return f'{h1} {ol}'

@app.route('/soma')
def soma_cal():
  n1 = 3.3
  n2 = 1.4
  resultado = soma(n1, n2) 
  h2 = f'<h2> A soma é: {resultado}</h2>'
  voltar = '<a href="/">Voltar</a>'
  return f'{h1} {h2} <br> {voltar}'

@app.route('/subtracao')
def subtracao_cal():
  n1 = 3.3
  n2 = 1.4
  resultado = subtracao(n1, n2)  
  h2 = f'<h2> A subtracao é: {resultado}</h2>'
  voltar = '<a href="/">Voltar</a>'
  return f'{h1} {h2} <br> {voltar}'

@app.route('/divisao')
def divisao_cal():
  n1 = 3.3
  n2 = 1.4
  resultado = divisao(n1, n2)
 
  h2 = f'<h2> A soma é: {resultado}</h2>'
  voltar = '<a href="/">Voltar</a>'
  return f'{h1} {h2} <br> {voltar}'

@app.route('/multiplicar')
def multiplicacao_cal():
  n1 = 3.3
  n2 = 1.4
  resultado = multiplicacao(n1, n2) 
  h2 = f'<h2> A soma é: {resultado}</h2>'
  voltar = '<a href="/">Voltar</a>'
  return f'{h1} {h2} <br> {voltar}'

app.run(debug = True)