import math
n = float(input('Digite um número:'))
print(f'O valor digitado é {n} e a sua porção inteira é {math.trunc(n)}')
print(f'O valor digitado é {n} e a sua porção inteira é {n:.0f}')

from math import trunc
n = float(input('Digite um número:'))
print(f'O valor digitado é {n} e a sua porção inteira é {trunc(n)}')
print(f'O valor digitado é {n} e a sua porção inteira é {int(n)}')