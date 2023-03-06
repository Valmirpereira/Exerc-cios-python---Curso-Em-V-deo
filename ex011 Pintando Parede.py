largura = float(input('largura da parede?'))
altura = float(input('altura da parede?'))
area = largura * altura
tinta = area / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m²')
print(f'para pintar essa parede, você precisará de {tinta}l de tinta.')