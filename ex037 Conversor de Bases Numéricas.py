'''numero = int(input('Digite um número para ser convertido: '))
bi     = numero % 2
oc     = oct(numero)
hex    =hex(numero)

print('O número {} convertido em binário é {}'.format(numero,bi))
print('O número {} convertido em octal é {}'.format(numero,oc))
print('O número {} convertido em hex é {}'.format(numero,hex))'''

'''print('-=-'*20)
print('Conversor de bases')
print('-=-'*20)
n   = input('Digite um número para converter: ')
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
opc = input('')
if opc == 1:
    print(n % 2)'''


num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if   opção == 1:
    print('{} Convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(num,(hex(num)[2:])))
else:
    print('Opção INVÁLIDA, Tente novamente.')