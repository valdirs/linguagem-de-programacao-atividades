''' 6. Crie um programa que gere e exiba os 100 primeiros números primos.'''
contador = 0
num = 2

while contador < 100:
    # Assumimos que o número é primo
    primo = True
    
    # Verificamos se o número é divisível por qualquer número entre 2 e num-1
    for i in range(2, num):
        if num % i == 0:
            primo = False  # O número não é primo
            break  # Se encontramos um divisor, saímos do loop

    # Se o número for primo, imprimimos e aumentamos o contador
    if primo:
        print(num)
        contador += 1
    
    
    num += 1 # Aumenta o número a ser verificado
