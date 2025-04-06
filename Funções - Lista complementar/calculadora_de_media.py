''' 4. Calculadora de Média:
○ Crie uma função que receba três notas e retorne a média do aluno.
○ Mostre se o aluno está aprovado ou reprovado (média mínima 7).'''
def calcular_media(a,b,c):
    return (a + b + c) / 3
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
print(f'A média do estudante foi: {calcular_media(n1,n2,n3)}')
media = calcular_media(n1,n2,n3)
if media < 7:
    print('Estudante reprovado!')
else:
    print('Estudante Aprovado!')
