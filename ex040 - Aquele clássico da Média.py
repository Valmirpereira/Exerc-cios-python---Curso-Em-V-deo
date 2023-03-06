'''n1    = float(input('Digite a primeira nota: '))
n2    = float(input('Digite a segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    float(print('Sua média foi de {}, você foi REPROVADO'.format(média)))
elif média >= 7:
    float(print('Sua média foi de {} você foi APROVADO'.format(média)))
else:
    print('Sua média foi de {} você está em RECUPERAÇÃO'.format(média))
'''



n1    = float(input('Primeira nota: '))
n2    = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print('tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2, média))
if 7 > média >= 5:
#if média >=5 and média < 7:#
    print('O aluno está em recuperação')
elif média < 5:
    print('O aluno está REPROVADO')
else:
    print('O aluno está APROVADO')