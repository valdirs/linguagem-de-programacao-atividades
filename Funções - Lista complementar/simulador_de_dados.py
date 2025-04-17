''' 7. Simulador de Dados:
○ Crie uma função que gere um número aleatório entre 1 e 6, simulando o
lançamento de um dado.'''
from random import randint
from time import sleep
def dado():
    n_sorteado = randint(1,6)
    return n_sorteado

print('-=' * 20)
print('O DADO FOI LANÇADO... E o número que caiu foi o')
print('...')
sleep(2)
print(f'{dado()}')
print('-=' * 20)