valorProduto   = float(input('Digite o valor do produto: R$'))
print('''Digite o código da opção de pagamento
[ 1 ] À VISTA/DINHEIRO ou CHEQUE
[ 2 ] À VISTA NO CARTÃO
[ 3 ] EM 2x NO CARTÃO
[ 4 ] EM 3x NO CARTÃO''')
desc1  = valorProduto * 10 / 100
desc2  = valorProduto *  5 / 100
juros4 = valorProduto * 20 / 100
opção = int(input('Digite o Código de pagamento '))
if opção == 1:
    print('A forma de pagamento escolhida foi À VISTA (10% de DESCONTO)')
    print('O valor a pagar será de R${:.2f}'.format(valorProduto - desc1))
elif opção == 2:
    print('A forma de pagamento escolhida foi À VISTA NO CARTÃO (5% de DESCONTO)')
    print('O valor a pagar será de R${:.2f}'.format(valorProduto - desc2))
elif opção == 3:
    print('A forma de pagamento escolhida foi em 2X NO CARTÃO')
    print('O valor a pagar será de R${:.2f}'.format(valorProduto))
elif opção == 4:
    print('A forma de pagamento escolhida foi EM 3x NO CARTÃO ')
    print('O valor a pagar será de R${:.2f}'.format(valorProduto + juros4))
else:
    print('Opção INVÁLIDA, tente novamente.')
