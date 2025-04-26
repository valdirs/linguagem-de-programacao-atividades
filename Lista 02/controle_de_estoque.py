''' Crie um sistema para gerenciar um pequeno estoque de produtos que deve:
- Permitir adicionar produtos com nome, quantidade e preço.
- Exibir todos os produtos cadastrados e o valor total do estoque.
- Armazenar os dados em um arquivo JSON.
'''
import json
import os

arquivo_estoque = 'controle_de_estoque.json'

# Carregar produtos do arquivo
def carregar_produtos():
    if os.path.exists(arquivo_estoque):
        with open(arquivo_estoque, 'r') as f:
            return json.load(f)
    else:
        return []

# Salvar produtos no arquivo
def salvar_produtos(produtos):
    with open(arquivo_estoque, 'w') as f:
        json.dump(produtos, f, indent=4)

# Adicionar um novo produto
def adicionar_produto(produtos):
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço (por unidade): "))
        produto = {
            'nome': nome,
            'quantidade': quantidade,
            'preco': preco
        }
        produtos.append(produto)
        salvar_produtos(produtos)
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Entrada inválida. Quantidade deve ser número inteiro e preço deve ser número decimal.")

# Exibir todos os produtos e o valor total do estoque
def exibir_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    valor_total = 0
    print("\n=== Produtos Cadastrados ===")
    for idx, produto in enumerate(produtos):
        subtotal = produto['quantidade'] * produto['preco']
        valor_total += subtotal
        print(f"{idx + 1}. {produto['nome']} - Quantidade: {produto['quantidade']} - Preço: R${produto['preco']:.2f} - Subtotal: R${subtotal:.2f}")

    print(f"\nValor total do estoque: R${valor_total:.2f}")

# Menu principal
def menu():
    produtos = carregar_produtos()
    while True:
        print("\n===== Controle de Estoque =====")
        print("1. Adicionar produto")
        print("2. Exibir produtos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_produto(produtos)
        elif opcao == '2':
            exibir_produtos(produtos)
        elif opcao == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()