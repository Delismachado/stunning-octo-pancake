# pip3 install flask
from flask import  Flask, render_template
from calc import soma, subtracao, divisao, multiplicacao

app = Flask(__name__)

h1 = '<h1>Calculadora...</h1>'
titulo = 'caluladora olist'

@app.route('/')


def index():
  lista = ['somar', 'subtrair', 'dividir']
  return render_template('index.html', titulo=titulo)
 

@app.route('/soma')
def soma_cal():
  n1 = 3.0
  n2 = 5.0
  resultado = soma(n1, n2) 
  return render_template('somar.html', resultado=resultado, titulo=titulo)

@app.route('/subtracao')
def subtracao_cal():
  n1 = 3.3
  n2 = 1.4
  resultado = subtracao(n1, n2)
  return render_template('subtrair.html', resultado=resultado, titulo=titulo)  
  

@app.route('/divisao')
def divisao_cal():
  n1 = 3.3
  n2 = 1.4
  resultado = divisao(n1, n2)
  return render_template('dividir.html', resultado=resultado, titulo=titulo)
 
  
@app.route('/multiplicar')
def multiplicacao_cal():
  n1 = 3.3
  n2 = 1.4
  resultado = multiplicacao(n1, n2) 
  return render_template('multiplicar.html', resultado=resultado, titulo=titulo)

app.run(debug = True)