segundos = int(input('Digite um valor em segundos para ver sua conversão em minutos, horas e dias: '))
minutos = segundos / 60
horas = segundos / 3600
dias = segundos / 86400
print('''Segundos convertidos para minutos é igual a : {} minutos.
Segundos convertidos em horas é igual a : {} horas.
E, Segundos convertidos para dias é igual a : {:.2f} dias.'''.format(minutos, horas, dias)) 