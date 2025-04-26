''' Desenvolva um sistema para controle de reservas de um evento que permita:
- Visualizar o mapa de assentos disponíveis.
- Reservar um assento específico.
- Cancelar uma reserva.
'''
import json
import os

arquivo_assentos = 'assentos.json'

FILEIRAS = 5
ASSENTOS_POR_FILEIRA = 10

# Carregar o mapa de assentos do arquivo
def carregar_assentos():
    if os.path.exists(arquivo_assentos):
        with open(arquivo_assentos, 'r') as f:
            return json.load(f)
    else:
        # Criar mapa inicial
        assentos = []
        for fileira in range(FILEIRAS):
            linha = ['Livre'] * ASSENTOS_POR_FILEIRA
            assentos.append(linha)
        salvar_assentos(assentos)
        return assentos

# Salvar o mapa de assentos no arquivo
def salvar_assentos(assentos):
    with open(arquivo_assentos, 'w') as f:
        json.dump(assentos, f, indent=4)

# Exibir o mapa de assentos
def exibir_assentos(assentos):
    print("\n=== Mapa de Assentos ===")
    for i, fileira in enumerate(assentos):
        linha = f"Fileira {i+1}: "
        for j, assento in enumerate(fileira):
            if assento == 'Livre':
                linha += f"[{j+1:02d}] "
            else:
                linha += "[XX] "
        print(linha)

# Reservar um assento específico
def reservar_assento(assentos):
    exibir_assentos(assentos)
    try:
        fileira = int(input("Escolha a fileira (1-5): ")) - 1
        numero = int(input(f"Escolha o número do assento (1-{ASSENTOS_POR_FILEIRA}): ")) - 1

        if assentos[fileira][numero] == 'Livre':
            nome = input("Digite o seu nome para a reserva: ")
            assentos[fileira][numero] = nome
            salvar_assentos(assentos)
            print("Assento reservado com sucesso!")
        else:
            print("Esse assento já está reservado.")
    except (IndexError, ValueError):
        print("Assento inválido. Tente novamente.")

# Cancelar uma reserva
def cancelar_reserva(assentos):
    exibir_assentos(assentos)
    try:
        fileira = int(input("Escolha a fileira do assento a cancelar (1-5): ")) - 1
        numero = int(input(f"Escolha o número do assento a cancelar (1-{ASSENTOS_POR_FILEIRA}): ")) - 1

        if assentos[fileira][numero] != 'Livre':
            assentos[fileira][numero] = 'Livre'
            salvar_assentos(assentos)
            print("Reserva cancelada com sucesso!")
        else:
            print("Esse assento já está livre.")
    except (IndexError, ValueError):
        print("Assento inválido. Tente novamente.")

# Menu principal
def menu():
    assentos = carregar_assentos()
    while True:
        print("\n===== Sistema de Reservas =====")
        print("1. Visualizar mapa de assentos")
        print("2. Reservar assento")
        print("3. Cancelar reserva")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            exibir_assentos(assentos)
        elif opcao == '2':
            reservar_assento(assentos)
        elif opcao == '3':
            cancelar_reserva(assentos)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()