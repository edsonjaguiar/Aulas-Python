núm = cont = soma = 0
núm = int(input('Digite um número [999 Para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 Para parar]: '))
print('você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
