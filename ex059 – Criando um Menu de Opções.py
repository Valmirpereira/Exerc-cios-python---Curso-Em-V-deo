from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('=-=' * 10)
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        resultado = v1 + v2
        print('O resultado de {} + {} é {}'.format(v1,v2,resultado))
    elif opção == 2:
        resultado = v1 * v2
        print('O resultado de {} x {} é {}'.format(v1,v2,resultado))
    elif opção == 3:
        if v1 > v2:
            maior = v1
            print('Entre {} e {} o maior valor é {}'.format(v1,v2,maior))
        else:
            maior = v2
            print('Entre {} e {} o maior valor é {}'.format(v1,v2,maior))
    elif opção == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('finalizando...')
    else:
        print('Opção inválida, Tente novamente')
    print('=-='* 10)
    sleep(2)
print('Fim do programa! Volte sempre!')

