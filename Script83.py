núm = int(input('Digite um número: '))
def Error():
    print('Um Erro Foi detectado')

while True:
    if núm <= 0:
        Error()
        break
    else:
        núm = int(input('Digite um número: '))
