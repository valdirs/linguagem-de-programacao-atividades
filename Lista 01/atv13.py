''' 13. Dado um salário inicial e um aumento percentual que dobra a cada ano, calcule o
salário atual após vários anos.'''
salario_inicial = 1000
anos = int(input('Digite a quantidade de anos para ver quanto seu salário aumentou neste período: '))

# Inicializando o aumento percentual
aumento_percentual = 0.10  # O aumento no primeiro ano será de 10%

# Calculando o novo salário após o número de anos
novo_salario = salario_inicial

for ano in range(anos):
    aumento = novo_salario * aumento_percentual  # Calculando o aumento do ano
    novo_salario += aumento  # Adicionando o aumento ao salário
    aumento_percentual *= 2  # O aumento dobra a cada ano

print(f'O seu salário após {anos} anos será R$ {novo_salario:.2f}')