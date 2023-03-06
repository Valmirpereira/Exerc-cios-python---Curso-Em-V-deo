print('=' *30)
print('{:^30}'.format('BANCO CEV'))
print('=' *30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
                       # esse código serve para verificar quantas vezes o programa vai tirar 50 do total
    if total >= céd:   # se o total for maior ou igual ao valor da cédula (50)
        total -= céd   #total vai ser total - essa cédula
        totcéd += 1    #somar o total de cédulas usadas para abater o total
    else:
        if totcéd > 0: # se o total for igual a 0 ele nao mostra
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:       # se a cédula atual for  igual a 50
            céd = 20        # a cédula passa a valer 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' *30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')