dist = int(input('Qual a distância á percorrer: '))
c1   = (dist*0.50)
c2   = (dist*0.45)
if dist>200:
    print('O valor da sua viagem será de R${:.2f}'.format(c2))
else:
    print('O valor da sua viagem será de R${:.2f}'.format(c1))


'''distância = float(input('Qual a distância da sua viagem?'))
print('Você está preste a começar uma viagem de {}Km.'.format(distância))
if distância<=200:
    preço=distância* 0.50
else:
    preço = distância*0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''


#if simplificado
'''distância = float(input('Qual a distância da sua viagem?'))
print('Você está preste a começar uma viagem de {}Km.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância* 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''