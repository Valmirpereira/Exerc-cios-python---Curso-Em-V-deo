nome=str(input('Digite seu nome:')).strip()
#o .strip no final do input ja vai tirar os espaços
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print(f'Seu nome em minúsculas é {nome.lower()}')
print('Seu nome em minúsculas é {}'.format(nome.lower()))
#nao consegui fazer esse dos dois jeitos

print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa=nome.split()
print(f'Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])} letras')
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))