from datetime import date
'''atual   = date.today().year
anoNasc = int(input('Digite o ano de nascimento do atléta: '))
idade   = atual - anoNasc
print('O atléta tem {} anos'.format(idade))
if 10 <= idade <=14:
    print('Classificação: INFANTIL')
elif idade <= 9:
    print('Classificação: MIRIM')
elif idade <=19:
    print('Classificação: JÚNIOR')
elif idade <=25:
    print('Classificação: SÊNIOR')
elif idade > 25:
    print('Classificação: MASTER')'''


atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atléta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <=14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')