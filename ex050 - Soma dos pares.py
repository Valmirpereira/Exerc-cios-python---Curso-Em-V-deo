soma = 0
cont = 0
for c in range (1, 7):
    num = int(input('Digite o {} valor:'.format(c)))
    if num % 2 ==0:
        soma = soma+num
        cont = cont + 1
if cont ==1:
    print('Você informou {} número par e a soma foi {}'.format(cont,soma))
elif cont == 0:
    print('Você não informou nenhum número par')
else:
    print('Você informou {} números pares e a soma foi {}'.format(cont, soma))