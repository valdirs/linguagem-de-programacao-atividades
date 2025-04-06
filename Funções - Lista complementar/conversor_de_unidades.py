''' 2. Conversor de Unidades:
- Crie funções para converter quilômetros em milhas, metros em
centímetros e litros em mililitros.'''
def km_em_milhas(km):
    return km * 0.6214

def m_em_cm(m):
    return m * 100

def L_em_mL(L):
    return L * 1000

km = float(input('Digite o valor em Km: '))
m = float(input('Digite o valor em metros: '))
L = float(input('Digite o valor em litros:'))

print(f'{km} km equivalem a {km_em_milhas(km):.2f} milhas.')
print(f'{m} metros equivalem a {m_em_cm(m)} cm.')
print(f'{L} litros equivalem a {L_em_mL(L)} ml.')