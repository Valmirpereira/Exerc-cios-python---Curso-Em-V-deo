valor = float(input('Qual é o preço do prodotu? R$'))
valor_com_desconto = valor - ( valor * 5 / 100)
#desconto = valor * 5 / 100
#valor_com_desconto = valor - desconto
print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custar R${valor_com_desconto:.2f}')