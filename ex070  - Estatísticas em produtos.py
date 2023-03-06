tot = 0
cont = 0
prodMil  = 0
menor = 0
barato = ' '
while True:
    print('-' * 30)
    print('LOJAS XABLAUS')
    print('-'*30)
    produto = str(input('Nome do produto: '))
    preço   = float(input('Preço: R$'))
    tot += preço
    cont += 1
    if preço >= 1000:
        prodMil += 1
    if  cont == 1:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp    = str(input('Quer continuar: [S/N] ')).upper()
    if resp == 'N':
        break
print(f'total gasto na compra foi de {tot:.2f}')
print(f'{prodMil} produtos custam mais de R$1000.00')
print(f'{barato} é o produto mais barato e custa R${menor:.2f}')

