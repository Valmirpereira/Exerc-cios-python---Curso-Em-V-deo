d = float(input('Uma distância em metros:'))
km  = d / 1000
hm  = d / 100
dam = d / 10
dm  = d * 10
cm  = d * 100
mm  = d * 1000
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dam')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')