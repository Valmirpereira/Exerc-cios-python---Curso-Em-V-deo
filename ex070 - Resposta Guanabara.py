total = totmil = menor = cont = 0
barato = 0
while True:    #looping infinito
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 :
        menor = preço    # rever aula 14 para entender
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    resp = ' '
    while resp not in 'SN': # se a resposta nao tiver S ou N o while nao vai parar
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0] #.strip tira os espaços [0] pegar apenas a primeira letra
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA')) #^ serve para centralizar
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000.00')
print(f'O menor produto mais barato foi {barato} que custa R${menor:.2f}')