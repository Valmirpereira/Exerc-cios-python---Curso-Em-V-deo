print('='*30)
print('{:^30}'.format('BANCO CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totCéd = 0
while True:
    if total >= céd:
        total -= céd
        totCéd += 1
    else:
        if totCéd > 0:
            print(f'Total de {totCéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totCéd = 0
        if total == 0:
            break

