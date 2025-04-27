print('''Em uma partida do campeonato pernambucano, entre Santa Cruz e Sport, na Ilha do Retiro,
o Jogo estava empatado em 1x1 aos 40 do 2° tempo. Surge uma chance do Santa Cruz desempatar o jogo aos 44. 
Tiaguinho corre pela lateral esquerda do campo, perto da grande área do gol do Sport, e faz um cruzamento rasteiro perfeito para Douglas Skillo, que está de frente para o gol... ''')
print('')
acao = input('O que aconteceu no lance de Skillo? : ').strip().upper()
print('')
print(f'E Douglas Skillo {acao.lower()}.')
if 'GOL' not in acao.split() :
    if 'PERDEU' or 'PERDE' or 'PERDENDO' in  acao.split() :
        print('Depois dessa chance perdida por Douglas Skillo, atacante do Santa Cruz, surge uma chance para o time do Sport, Gonçalo Paciência recebe de Lucas Lima um toque enfiado, que faz com que Paciência fique cara a cara com RoKenedy, e Paciência...')
    print('')
    acao2 = input('O que acontece nesse lance? : ').strip().upper()
    print('')
    print(f'Paciência {acao2.lower()}.')
    if 'GOL' not in acao2.split() :
        if 'PERDEU' or 'PERDE' or 'PERDENDO' in acao2.split() : 
            print(f'O jogo acaba empatado, na Ilha do Retiro, com erro dos jogadores das 2 equipes, que perderam oportunidades de levar a vitória para casa.')
    else:
        print(f'Paciência faz um lance em que  {acao2.lower()} que faz com que o Sport se consagre vencedor deste clássico das multidões, em sua casa, por 2x1, após a chance perdida por Douglas Skillo.')