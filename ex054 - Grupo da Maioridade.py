from datetime import date
anoAtual = date.today().year
totMaior = 0
totMenor = 0
for pess in range(1,8):
    anoNasc  = int(input('Em que ano a pessoa nasceu? '))
    idade    = anoAtual - anoNasc
    if idade >=21:
        totMaior += 1
    else:
        totMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totMaior))
print('E também tivemos {} pessoas menores de idade'.format(totMenor))
