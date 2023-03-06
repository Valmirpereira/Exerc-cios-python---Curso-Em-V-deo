from random import randint
win = 0
while True:
    print('-='*30)
    pc         = randint(0,10)
    j1         = int(input('Diga um valor : '))
    soma = pc + j1
    if soma % 2 == 0:
        parOUimpar = str(input('Par ou Ímpar [P/I] ')).upper()
        if parOUimpar == 'P':
            print(f'Você jogou {j1} e o computador {pc}. Total de {soma} DEU PAR')
            print('Você VENCEU')
            print('Vamos jogar novamente')
            win += 1
        if parOUimpar == 'I':
            print(f'Você jogou {j1} e o computador {pc}. Total de {soma} DEU PAR')
            print('Você PERDEU')
            break
    if soma % 2 != 0:
        parOUimpar = str(input('Par ou Ímpar [P/I] ')).upper()
        if parOUimpar == 'I':
            print(f'Você jogou {j1} e o computador {pc}. Total de {soma} DEU ÍMPAR')
            print('Você VENCEU')
            print('Vamos jogar novamente')
            win += 1
        if parOUimpar == 'P':
            print(f'Você jogou {j1} e o computador {pc}. Total de {soma} DEU ÍMPAR')
            print('Você PERDEU')
            break
print(f'GAME OVER! Você venceu {win} vezes')