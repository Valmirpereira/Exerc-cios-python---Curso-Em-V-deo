'''s = 'M'
s = 'F'
while s == 'M' or s == 'F':
    s = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
    if s != 'M' and s != 'F':
            s = input('Dados inválidos. Por favor, informe seu sexo: ').upper()
    if s == 'M' or s == 'F':
        print('Sexo {} registrado com sucesso'.format(s))'''


sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))