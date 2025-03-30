''' 1. Peça ao usuário três notas e calcule: a. A média aritmética simples
b. A média ponderada considerando os pesos 2, 2 e 3
c. A média ponderada considerando os pesos 1, 2 e 2 '''
# 1.
n1 = float(input('Digite a 1° nota : '))
n2 = float(input('Digite a 2° nota : '))
n3 = float(input('Digite a 3° nota : '))
media_aritmetica = (n1 + n2 + n3) / 3

p1 = 2
p2 = 2
p3 = 3
media_ponderada = ((n1*p1)+(n2*p2)+(n3*p3))/(p1 + p2 + p3)

p_1=1
p_2=2
p_3=2
media_ponderada2 = ((n1*p_1) + (n2*p_2) + (n3*p_3)) / (p_1 + p_2 + p_3)
print(f'A) Média aritmética: {media_aritmetica:.2f}')
print(f'B) Média ponderada (pesos 2, 2, 3): {media_ponderada:.2f}')
print(f'C) Média ponderada (pesos 1, 2, 2): {media_ponderada2:.2f}')