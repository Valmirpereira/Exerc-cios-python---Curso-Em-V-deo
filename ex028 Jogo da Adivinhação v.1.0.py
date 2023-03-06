#import random
#num = random.randint(0,5)
#n   = int(input('Adivinhe o número de 0 á 5 :'))
#if n == num:
#    print('PARABÉNS! Você Conseguiu me vencer')
#else:
#    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num,n))

from random import randint
from time import sleep  # Faz o computador aguardar algum tempo que eu escolher
computador = randint(0,5) #Faz o computador ''pensar''
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) # jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)    #espera quantos segundos para aparecer
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador,jogador))