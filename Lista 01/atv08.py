''' 8. Solicite uma temperatura em Celsius e converta para Fahrenheit.'''
temperatura_em_C = float(input('Digite uma temperatura em °C para convertê-la em °F: '))
temperatura_em_F = (temperatura_em_C * 1.8) + 32
print(f'{temperatura_em_C:.1f}°C equivalem a {temperatura_em_F:.1f}°F.')