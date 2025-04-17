''' 8. Verificador de Palíndromos:
○ Crie uma função que receba uma palavra e diga se ela é um palíndromo
(lê igual de frente para trás).'''
def verificar_palindromos(palavra):
    palavra = palavra.lower().replace(' ', '')
    return palavra == palavra[::-1]#  Faz a palavra ser lida de trás para frente, isso chama-se tratamento de strings.

palavra = input('Digite a palavra ou frase(Sem acentos) para verificarmos se ela é um palíndromo ou não: ')
if verificar_palindromos(palavra):
    print(f'"{palavra}" é um palíndromo.')
else:
    print(f'"{palavra}" NÃO é um palíndromo.')