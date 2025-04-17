''' 5. Gerador de Tabuada:
○ Crie uma função que receba um número e imprima a tabuada desse
número.'''
def tabuada(x):
    for i in range(1,11):
        if i > 10:
            break
        else:
            print(f'{x} x {i} = {x * i}')
x = int(input('Digite um número para ver sua tabuada - Até o 10° termo: '))
print(tabuada(x))