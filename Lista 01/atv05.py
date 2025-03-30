''' 5. Imprima os 100 primeiros números naturais na tela.'''

for x in range(1, 101):
    if x < 100: # Os números menores que 100 são separados por " / "
        print(x, end = " / ")
    else: # O último número 100, não será separado por " / " já que é o último número.
        print(x)