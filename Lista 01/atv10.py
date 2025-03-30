''' 10. Solicite um número inteiro maior que 1 e verifique se ele é primo.'''
n = int(input('Digite um número inteiro maior que 1, para verificarmos se ele é um número primo: '))
if n <= 1:
    print(f'{n} não é um número primo, pois para verificarmos se um número é primo, o número tem que ser maior que 1.')
else:
    for x in range(2, n):
        if n % x == 0: # n % i == 0: O operador % verifica se o número n é divisível por i. Se o resto da divisão for 0 (n % i == 0), significa que n é divisível por i, então ele não é primo
            print(f'{n} não é um número primo.')
            break # Interrompe o laço porque achou um valor no intervalo do laço que n é divisível.
    else:
        print(f'{n} é um número primo.')