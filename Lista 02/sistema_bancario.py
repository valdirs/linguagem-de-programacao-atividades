''' Crie um sistema bancário simples que permita:
- Login de usuários (com nome de usuário e senha).
- Depósitos e saques.
- Registro das transações realizadas.
'''
import json
import os

arquivo_usuarios = 'usuarios.json'

# Carregar dados dos usuários
def carregar_usuarios():
    if os.path.exists(arquivo_usuarios):
        with open(arquivo_usuarios, 'r') as f:
            return json.load(f)
    else:
        return {}

# Salvar dados dos usuários
def salvar_usuarios(usuarios):
    with open(arquivo_usuarios, 'w') as f:
        json.dump(usuarios, f, indent=4)

# Criar um novo usuário
def criar_usuario(usuarios):
    nome = input("Escolha um nome de usuário: ")
    if nome in usuarios:
        print("Usuário já existe.")
        return

    senha = input("Escolha uma senha: ")
    usuarios[nome] = {
        'senha': senha,
        'saldo': 0.0,
        'transacoes': []
    }
    salvar_usuarios(usuarios)
    print("Usuário criado com sucesso!")

# Fazer login
def login(usuarios):
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")

    if nome in usuarios and usuarios[nome]['senha'] == senha:
        print(f"Bem-vindo(a), {nome}!")
        return nome
    else:
        print("Usuário ou senha incorretos.")
        return None

# Realizar depósito
def deposito(usuarios, usuario):
    try:
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            usuarios[usuario]['saldo'] += valor
            usuarios[usuario]['transacoes'].append(f"Depósito de R${valor:.2f}")
            salvar_usuarios(usuarios)
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido.")
    except ValueError:
        print("Entrada inválida.")

# Realizar saque
def saque(usuarios, usuario):
    try:
        valor = float(input("Valor do saque: "))
        if 0 < valor <= usuarios[usuario]['saldo']:
            usuarios[usuario]['saldo'] -= valor
            usuarios[usuario]['transacoes'].append(f"Saque de R${valor:.2f}")
            salvar_usuarios(usuarios)
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")
    except ValueError:
        print("Entrada inválida.")

# Exibir extrato
def extrato(usuarios, usuario):
    print("\n=== Extrato ===")
    for transacao in usuarios[usuario]['transacoes']:
        print(transacao)
    print(f"Saldo atual: R${usuarios[usuario]['saldo']:.2f}")

# Menu principal após login
def menu_usuario(usuarios, usuario):
    while True:
        print("\n===== Menu Bancário =====")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            deposito(usuarios, usuario)
        elif opcao == '2':
            saque(usuarios, usuario)
        elif opcao == '3':
            extrato(usuarios, usuario)
        elif opcao == '4':
            print("Saindo da conta...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Menu inicial
def menu():
    usuarios = carregar_usuarios()
    while True:
        print("\n===== Sistema Bancário =====")
        print("1. Criar novo usuário")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            criar_usuario(usuarios)
        elif opcao == '2':
            usuario = login(usuarios)
            if usuario:
                menu_usuario(usuarios, usuario)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    menu()