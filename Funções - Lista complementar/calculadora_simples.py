''' 1. Calculadora Simples:
- Crie funções para soma, subtração, multiplicação e divisão.
- Faça um programa que peça dois números e mostre o resultado da
operação escolhida.'''
def soma(x,y):
    return x + y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x * y

def divisao(x,y):
    if y == 0:
        return 0
    else:
        return x / y 

x = float(input('Valor de x: '))
y = float(input("Valor de y: "))
operacao = input('''Qual operação você deseja? 
[+] => Para somar os valores
[-] => Para achar a diferença entre os valores
[*] => Para multiplicar um valor pelo outro
[/] => Para dividir o primeiro valor pelo segundo valor

Digite o símbolo da operação que você deseja(E não adicione mais nada): ''').strip()
if operacao == "+":
     print(f'{x} {operacao} {y} = {soma(x,y)}' )
elif operacao == "-":
     print(f'{x} {operacao} {y} = {subtracao(x,y)}' )
elif operacao == "x":
     print(f'{x} {operacao} {y} = {multiplicacao(x,y)}' )
elif operacao == '/':
    print(f'{x} {operacao} {y} = {divisao(x,y)}' )
else:
    print('Operação Inválida!')