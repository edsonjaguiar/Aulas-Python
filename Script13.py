nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if média >= 7.0:
    print('Aprovado')
elif média <= 5.0 or 6.9:
    print('Recuperação')
elif média < 5.0:
    print('REPROVADO')
