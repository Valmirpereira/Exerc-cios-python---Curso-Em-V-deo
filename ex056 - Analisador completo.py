maior      = 0
menor      = 0
feminino   = 0
masculino  = 0
for c in range (1,5):
    print('----- {}ª PESSOA -----'.format(c))
    nome  = str(input('Nome: '.format(c)))
    idade = int(input('Idade: '.format(c)))
    if c == 1:
        maior = idade
        menor = idade
        media = idade + c / 2
    else:
        if idade > maior:
            maior = idade
        if idade < menor:
            menor = idade
    sexo  = str(input('Sexo [M/F]: '.format(c)))
    m = 1
    f = 2
    m +=1
    f +=1
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior,nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(f))