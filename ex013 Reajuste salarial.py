salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + ( salario * 15 / 100 )
input(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento passa a receber R${aumento:.2f}')