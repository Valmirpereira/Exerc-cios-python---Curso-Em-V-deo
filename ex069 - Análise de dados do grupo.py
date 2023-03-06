masc    = 0
idade18 = 0
femin20  = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-'*30)
    idade = int(input('Idade: '))
    if idade >= 18:
        idade18 += 1
    sx   = str(input('Sexo [M/F]: ')).upper()
    if sx == 'M':
        masc += 1
    if sx == 'F' and idade <= 20:
        femin20 += 1
    opc  = str(input('Quer continuar? [S/N] ')).upper()
    if opc == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {idade18}')
if masc > 1:
    print(f'Ao todo temos {masc} homens cadastrados')
if masc == 1:
    print(f'Ao todo temos {masc} homem cadastrado')
if femin20 >1:
    print(f'E temos {femin20} mulheres com menos de 20 anos')
if femin20 == 1:
    print(f'E temos {femin20} mulher com menos de 20 anos')