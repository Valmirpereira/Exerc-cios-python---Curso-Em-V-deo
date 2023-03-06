print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
termo  = int(input('Primeiro Termo: '))
razão  = int(input('Razão: '))
décimo = termo + (10 - 1) * razão
for p in range(termo,décimo + razão, razão):
    print('{} '.format(p),end=' ')
print('ACABOU')