''' 2. Solicite um valor em segundos e converta para dias, horas e minutos.'''

segundos = int(input('Digite um valor em segundos para ver sua conversão em minutos, horas e dias: '))
minutos = segundos / 60
horas = segundos / 3600
dias = segundos / 86400
print('''Segundos convertidos para minutos é igual a : {:.2f} minutos.
Segundos convertidos em horas é igual a : {:.2f} horas.
E, Segundos convertidos para dias é igual a : {:.2f} dias.'''.format(minutos, horas, dias)) 