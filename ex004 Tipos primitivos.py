n=input('Digite algo:')
print('O tipo primitivo desse valor é',type(n))
#print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Só tem espaço?             {n.isspace()}')
print(f'É numérico?                {n.isnumeric()}')
print(f'É alfabetico?              {n.isalpha()}')
print(f'É alfanumérico?            {n.isalnum()}')
print(f'Está em letra maiúscula?   {n.isupper()}')
print(f'Está em letra minúscula?   {n.islower()}')
print(f'Está capitaliada?          {n.istitle()}')


