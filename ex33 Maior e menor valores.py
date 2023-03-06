'''n1 = int(input('primeiro valor: '))
n2 = int(input('Segundo valor: '))
if n1>n2:
    print('{} é maior que {}'.format(n1,n2))
else:
    print('{} é maior que {}'.format(n2,n1))'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
#verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))