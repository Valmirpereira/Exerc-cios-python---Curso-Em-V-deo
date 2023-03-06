d  = float(input('Quantos dias alugados?'))
km = float(input('Quanto km foram percorridos? '))
valor = (d * 60) + (km * 0.15)
#km_valor = km * 0.15
#vl = d_valor + km_valor
print(f'O valor a ser pago é R${valor:.2f}')