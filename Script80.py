def área(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m²') 

print('-' * 22)
print('Controle de Terrenos')
print('-' * 22)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO(m): '))
área(l, c)
          
