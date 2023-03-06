'''from random import randint
palpites = 0
pc = int(randint(0,10))
print('Sou seu computador')
print('Acabei de pensar em um número')
j = int(input('Qual é o seu palpite? '))
if j == pc:
    print('PARABÉNS, VOCÊ ACERTOU')
while j != pc:
    if j < pc:
        print('Mais...Tente mais uma vez.')
        j = int(input('Qual é o seu palpite? '))
        if j == pc:
            print('PARABÉNS, VOCÊ ACERTOU')
    if j > pc:
        print('Menos...Tente mais uma vez.')
        j = int(input('Qual é o seu palpite? '))
        if j == pc:
            print('PARABÉNS, VOCÊ ACERTOU')
print('Você acertou com {} tentativas'.format(palpites))'''



from random import randint
pc = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez.')
        elif jogador > pc:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas, PARABÉNS!'.format(palpites))
