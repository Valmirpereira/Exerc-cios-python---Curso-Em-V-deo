'''data   = int(input('Digite seu ano de nascimento: '))
idade  = 2022 - data

print(idade)
if idade < 18 and:
    print('Você ainda não precisa se alistar')
elif idade == 18:
    print('Você deve se alistar')
else :
    print('Já passou do tempo de alistamento')'''

from datetime import date #Puxar a data atual no pc
atual = date.today().year
nasc  = int(input('Ano de nascimento: '))
idade = atual - nasc
print('''Qual Seu Sexo
[ 1 ] Masculino
[ 2 ] Feminino''')
opção=int(input('Digite sua opção: '))
if opção == 2:
    print('Você não precisa fazer o alistamento militar')
elif idade == 18 and 1:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade < 18 and 1:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano   = atual + saldo
    print('Seu alistamento será em {}'.format(saldo))
elif idade > 18 and 1:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    saldo = idade - 18
    print('Você ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
