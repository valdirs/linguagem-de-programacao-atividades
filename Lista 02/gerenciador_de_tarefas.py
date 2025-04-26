''' Implemente um sistema de gerenciamento de tarefas que permita:
- Adicionar tarefas com descrição e prazo.
- Listar as tarefas ordenadas por prazo.
- Marcar tarefas como concluídas.
- Armazenar os dados em um arquivo JSON para persistência.
'''
import json
import os
from datetime import datetime

arquivo_de_tarefas = 'gerenciador_de_tarefas.json'

# Carregar tarefas do arquivo
def carregar_tarefas():
    if os.path.exists(arquivo_de_tarefas):
        with open(arquivo_de_tarefas, 'r') as f:
            return json.load(f)
    else:
        return []

# Salvar tarefas no arquivo
def salvar_tarefas(tarefas):
    with open(arquivo_de_tarefas, 'w') as f:
        json.dump(tarefas, f, indent=4)

# Adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    descricao = input("Descrição da tarefa: ")
    prazo = input("Prazo (formato DD-MM-YYYY): ")
    tarefa = {
        'descricao': descricao,
        'prazo': prazo,
        'concluida': False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa adicionada com sucesso!")

# Listar tarefas ordenadas por prazo
def listar_tarefas(tarefas):
    tarefas_ordenadas = sorted(tarefas, key=lambda x: x['prazo'])
    for idx, tarefa in enumerate(tarefas_ordenadas):
        status = "Concluída" if tarefa['concluida'] else "Pendente"
        print(f"{idx + 1}. {tarefa['descricao']} - Prazo: {tarefa['prazo']} - Status: {status}")

# Marcar uma tarefa como concluída
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        num = int(input("Número da tarefa a concluir: "))
        if 1 <= num <= len(tarefas):
            tarefas_ordenadas = sorted(tarefas, key=lambda x: x['prazo'])
            tarefa = tarefas_ordenadas[num - 1]
            tarefa['concluida'] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

# Menu principal
def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n===== Gerenciador de Tarefas =====")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()