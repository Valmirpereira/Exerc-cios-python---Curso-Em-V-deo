casa      = float(input("Valor da casa: R$"))
salario   = float(input("Salário do comprador: R$"))
anos      = float(input("Quantos anos de financiamento?"))
prestação = casa / (anos * 12)
minimo    = salario * 30 / 100
print('para pagar a casa de R${:.2f} em {:.0f} anos a prestação será de R${:.2f} '.format(casa,anos,prestação))
if prestação <= minimo:
    print("Financiamento APROVADO")
else:
    print("Financiamento NEGADO")
#ESTUDAR MAIS SOBRE ESTE EXERCÍCIO





casa      = float(input('Valor da casa: R$'))
salario   = float(input('Salário do comprador: R$'))
anos      = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo    = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} '.format(casa,anos,prestacao))
#print('COMPARANDO tem que pagar {} e o mínimo é de {}'.format(prestacao,minimo))
if minimo >= prestacao:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')