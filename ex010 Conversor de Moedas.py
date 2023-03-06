#real = float(input('Quanto dinheiro você tem na carteira? R$'))
#dolar = real / 4.70
#print(f'Com R${real:.2f} você pode comprar US${dolar:.2f}')
#print('Com R${:.2f} você pode comprar US${:.2f}'.format(carteira,dolar))

dolar = float(input('Digite a cotação do dolar hoje: US$'))
real  = float(input('dinheiro em carteira: R$'))
print(f'Com R${real} você pode comprar US${real/dolar:.2f}')