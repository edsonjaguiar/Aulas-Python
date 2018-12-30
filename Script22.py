sexo = str(input('Digite seu Sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados Inválidos,Por favor digite a letra correta: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))

