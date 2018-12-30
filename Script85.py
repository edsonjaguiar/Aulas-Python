def leiaInt(n):
    while True:
        n = n.replace(' ','')
        if n.isnumeric():
            return n
        else:
            print('Erro! Digite um número inteiro válido')
            n = leiaInt(input('Digite um número: '))
n = leiaInt(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}.')
