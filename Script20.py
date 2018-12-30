from random import randint
computador = randint(0, 10)
print('-=' * 36)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10')
print('Será q você consegue adivinhar qual foi? ')
print('-=' * 36)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print('Acerto Mizeravi com {} tentativas.Parabéns!'.format(palpites))        

