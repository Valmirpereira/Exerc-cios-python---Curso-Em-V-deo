import math
ang = float(input('Digite o ângulo que você deseja:'))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print(f'O angulo de {ang} tem o SENO de {s:.2f}')
print(f'O angulo de {ang} tem o COSSENO de {c:.2f}')
print(f'O anglo de {ang} tem a TANGENTE de {t:.2f}')

from math import radians,sin,cos,tan

ang = float(input('Digite o ângulo que você deseja:'))
s = sin(sin(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print(f'O angulo de {ang} tem o SENO de {s:.2f}')
print(f'O angulo de {ang} tem o COSSENO de {c:.2f}')
print(f'O anglo de {ang} tem a TANGENTE de {t:.2f}')