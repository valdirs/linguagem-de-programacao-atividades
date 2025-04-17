''' 6. Contador de Vogais:
○ Crie uma função que conte quantas vogais existem em uma palavra ou
frase.'''
def contador_de_vogais(frase):
    vogais = 'aeiouáéíóúâêôãõà'
    contagem = 0
    for letra in frase:
        if letra in vogais:
            contagem += 1
    return contagem
    
frase = input('Digite a frase escolhida para ver quantas vogais tem na frase: ').lower()
print(f'A frase "{frase}" tem {contador_de_vogais(frase)} vogais.')
