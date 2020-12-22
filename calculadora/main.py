from calc import soma, divisao, multiplicacao, subtracao

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

print(f''' 
        [1] somar
        [2] subtrair
        [3] dividir
        [4] multiplicar
        [5] sair ''')

opr = input('Digite a operação que deseja realizar :) ')
if opr == "1":
  resultado = soma(numero1, numero2)
elif opr == "2":
  resultado = subtracao(numero1, numero2)
elif opr == "3":
  resultado = divisao(numero1, numero2)
elif opr == "4":
  resultado = multiplicacao(numero1, numero2)
elif opr == 5:
  exit(0)
else: 
  print('Operação inválida!')
  resultado = 0
  
print('Resultado:', resultado)