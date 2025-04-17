''' 3. Contagem de Caracteres:
○ Crie uma função que receba uma frase e conte quantos caracteres (sem
espaço) ela possui. '''
def contador_de_caracteres(frase):
    frase_sem_espacos = frase.replace(" ", "") # Remove os espaços
    return len(frase_sem_espacos) # Conta os caracteres, sem os espaços

frase = input('Digite aqui a frase escolhida: ').strip()
quantidade_de_caracteres = contador_de_caracteres(frase)
print(f'A frase que você digitou tem {quantidade_de_caracteres} caracteres(Sem contar com os espaços).')