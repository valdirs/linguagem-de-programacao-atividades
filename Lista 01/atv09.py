''' 9. Peça três números ao usuário e informe qual é o maior e qual é o menor.'''
n1 = float(input('Digite o 1° dos 3 números para ver qual é o maior: '))
n2 = float(input('Digite o 2° número: '))
n3 = float(input('Digite o 3° número: '))
if n1 == n2 == n3:
    print('Todos os números são iguais.')
else:
    if n1 > n2 and n1 >= n3:
        maior = n1
    elif n2 >= n1 and n2 >= n3:
        maior = n2
    else:
        maior = n3

    if n1 <= n2 and n1 <= n3:
        menor = n1
    elif n2 <= n1 and n2 <= n3:
        menor = n2
    else:
        menor = n3
    print(f'o maior número é: {maior:.1f} e o menor número é: {menor:.1f}.')
