'''peso   = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc    = peso / (altura * altura)
if imc <= 18.5:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('ABAIXO DO PESO NORMAL')
elif imc <= 25:
     print('Seu IMC é de {:.1f}'.format(imc))
     print('PESO IDEAL')
elif imc <= 30:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('SOBREPESO')
elif imc <= 40:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('OBESIDADE')
else:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('OBESIDADE MÓRBIDA')'''

peso    =float(input('Qual é o seu peso (Kg) '))
altura  =float(input('Qual é a sua altura? (m) '))
imc     = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO')
elif imc >= 30 and imc <40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
