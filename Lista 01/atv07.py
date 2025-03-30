''' 7. Solicite um número ímpar ao usuário e calcule a diferença entre o quadrado do número anterior e do próximo número ímpar.'''
num = int(input('Digite um número ímpar qualquer: '))


if num % 2 != 0: # Verifica se o número é ímpar
    anterior = num - 2
    proximo = num + 2
    # Calculando os quadrados
    quadrado_anterior = anterior ** 2
    quadrado_proximo = proximo ** 2

    diferenca = quadrado_proximo - quadrado_anterior # Diferença dos quadrados.

    print(f'A diferença entre o quadrado de {anterior} e {proximo} é: {diferenca}')
else:
    print('O número digitado não é ímpar.')
