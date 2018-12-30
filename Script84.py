def ficha(nome='<Desconhecido>', gols=0):
    print(f'O Jogador {nome} Fez {gols} gol(s) no campeonato.')

nome = str(input('Nome Do Jogador: '))
gols = str(input('Número de gol(s) '))
if gols == '':
    gols = 0
    
if nome == '':
    nome = '<Desconhecido>'   
ficha(nome, gols)
