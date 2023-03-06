n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('-' *30)
    for c in range(1,11):
        r = n * c
        print(f'{n} x {c} = {r}')
    print('-' * 30)
print('Programa tabuada encerrado. Volte sempre.'.upper())