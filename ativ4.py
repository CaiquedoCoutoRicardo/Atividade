lista_de_compras = []


def adicionar_item(item):
    lista_de_compras.append(item)
    print(f"{item} foi adicionado à lista de compras.")


def remover_item(item):
    if item in lista_de_compras:
        lista_de_compras.remove(item)
        print(f"{item} foi removido da lista de compras.")
    else:
        print(f"{item} não foi encontrado na lista de compras.")

def editar_item(item_antigo, item_novo):
    if item_antigo in lista_de_compras:
        index = lista_de_compras.index(item_antigo)
        lista_de_compras[index] = item_novo
        print(f"{item_antigo} foi editado para {item_novo}.")
    else:
        print(f"{item_antigo} não foi encontrado na lista de compras.")


def listar_itens():
    if lista_de_compras:
        print("Itens na lista de compras:")
        for item in lista_de_compras:
            print(item)
    else:
        print("A lista de compras está vazia.")


while True:
    print("\nOpções:")
    print("1. Adicionar item à lista de compras")
    print("2. Remover item da lista de compras")
    print("3. Editar item na lista de compras")
    print("4. Listar itens na lista de compras")
    print("5. Sair do programa")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        item = input("Digite o item que deseja adicionar: ")
        adicionar_item(item)
    elif escolha == '2':
        item = input("Digite o item que deseja remover: ")
        remover_item(item)
    elif escolha == '3':
        item_antigo = input("Digite o item que deseja editar: ")
        item_novo = input("Digite o novo valor para o item: ")
        editar_item(item_antigo, item_novo)
    elif escolha == '4':
        listar_itens()
    elif escolha == '5':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")






