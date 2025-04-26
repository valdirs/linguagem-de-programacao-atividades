''' Implemente um sistema de contatos que permita:
- Adicionar novos contatos com nome, telefone e email.
- Buscar contatos pelo nome.
- Armazenar os contatos em um arquivo JSON.
'''
import json
import os

arquivo_contatos = 'contatos.json'

# Carregar contatos do arquivo
def carregar_contatos():
    if os.path.exists(arquivo_contatos):
        with open(arquivo_contatos, 'r') as f:
            return json.load(f)
    else:
        return []

# Salvar contatos no arquivo
def salvar_contatos(contatos):
    with open(arquivo_contatos, 'w') as f:
        json.dump(contatos, f, indent=4)

# Adicionar novo contato
def adicionar_contato(contatos):
    nome = input("Nome do contato: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email
    }
    contatos.append(contato)
    salvar_contatos(contatos)
    print("Contato adicionado com sucesso!")

# Buscar contato pelo nome
def buscar_contato(contatos):
    busca = input("Digite o nome para buscar: ").lower()
    encontrados = []

    for contato in contatos:
        if busca in contato['nome'].lower():
            encontrados.append(contato)

    if encontrados:
        print("\n=== Contatos Encontrados ===")
        for c in encontrados:
            print(f"Nome: {c['nome']}, Telefone: {c['telefone']}, Email: {c['email']}")
    else:
        print("Nenhum contato encontrado com esse nome.")

# Menu principal
def menu():
    contatos = carregar_contatos()
    while True:
        print("\n===== Gerenciador de Contatos =====")
        print("1. Adicionar novo contato")
        print("2. Buscar contato pelo nome")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            buscar_contato(contatos)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()