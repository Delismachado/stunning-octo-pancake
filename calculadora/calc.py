def valida_float(numero: float) -> float:
  if isinstance(numero, float):
    return True
  raise ValueError(f'Valor informado {numero} não é numerico')

def soma(n1: float, n2: float) -> float:
  if valida_float(n1) and valida_float(n2):
    soma = n1 + n2
    return soma

def divisao(n1: float, n2: float) -> float:
  if valida_float(n1) and valida_float(n2):
    try:
      divisao = n1 / n2
    except:
        print('Erro de divisão por 0')
    return divisao

def multiplicacao(n1: float, n2: float) -> float:
  if valida_float(n1) and valida_float(n2):
    multiplicacao = n1 * n2
    return multiplicacao

def subtracao(n1: float, n2: float) -> float:
  if valida_float(n1) and valida_float(n2):
    subtracao = n1 - n2
    return subtracao