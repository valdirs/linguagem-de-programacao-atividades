''' 4. Um cliente alugou um carro e rodou alguns quilômetros por um certo número de
dias. O custo diário é de R$90. Se ele rodou mais de 100 km, há uma taxa extra de
R$12 por km adicional. Calcule o valor total a ser pago.'''

dias = int(input('Digite aqui, por quantos dias você alugou o automóvel : '))
distancia = float(input('Digite quantos Km você rodou no total : '))
valor = dias * 90
if distancia > 100:
    taxa = (distancia - 100) * 12
    valor += taxa
print('Você terá de pagar R${:.2f} ao total.'.format(valor))
