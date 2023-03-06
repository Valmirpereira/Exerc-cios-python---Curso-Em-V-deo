soma = 0
cont = 0
for n in range(1,501, 2):
    if n % 3 == 0:
        cont = cont + 1   #(Soma de valores que sao divisiveis por 3)
        soma = soma + n   #(Soma um valor)
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))
