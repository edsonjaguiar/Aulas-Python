from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou Pensar em um número entre 0 e 5.Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em Que Número eu pensei?: ')) # Jogador Tenta Adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você Conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador, jogador))

