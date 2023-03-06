#carro= int(input('Qual é a velocidade atual do carro? '))
#vp= 80
#m = int((-vp)+(carro))
#vl= float(m*7)
#if vp<carro:
   # print('Você ultrapassou {}km a mais do limite de velocidade e foi multado em R${:.2f}!'.format(m,vl)) #:.2f é para formatar a quantidade de zeros no float
#else:
   # print('Tenha um bom dia! Dirija com segurança!')



#Estrutura de condição simples (apenas com if)
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('MULTADO! você excedeu o limite permitido que é de 80km/h')
    multa = (velocidade-80)*7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')