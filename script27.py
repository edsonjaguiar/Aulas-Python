soma = 0
cont = 0
while True:
    núm = int(input('Digite um número: '))
    if núm == 999:
        break
    soma += núm
    cont += 1
print(f'A soma dos {cont} valores foi {soma}')
