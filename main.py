# Definição do menu de pizzas
menu_de_pizzas = {
    1: {"nome": "Pizza de Queijo", "preco": 25.99},
    2: {"nome": "Pizza de Calabresa", "preco": 28.99},
    3: {"nome": "Pizza de Frango com Catupiry", "preco": 30.99},
    4: {"nome": "Pizza de Bacon", "preco": 27.99}
}

print("Bem-vindo a Pizzaria del Gatitto")

# Exibir o menu de pizzas
print("===== Menu de Pizzas =====")
for numero, pizza in menu_de_pizzas.items():
    print(f"{numero}. {pizza['nome']} - R${pizza['preco']:.2f}")
print("==========================")

# Selecionar uma pizza
while True:
    selecao = input("Digite o número da pizza desejada: ")
    if selecao.isdigit() and int(selecao) in menu_de_pizzas:
        break
    else:
        print("Por favor, digite um número de pizza válido.")

# Informar a quantidade
while True:
    quantidade = input("Digite a quantidade de pizzas desejada: ")
    if quantidade.isdigit() and int(quantidade) > 0:
        break
    else:
        print("Por favor, digite uma quantidade válida.")

# Escolher opção de entrega
entrega = input("Deseja entrega? (s/n): ")
while entrega.lower() not in ['s', 'n']:
    entrega = input("Opção inválida. Digite 's' para entrega ou 'n' para não entrega: ")

# Calcular o preço total do pedido
preco_unitario = menu_de_pizzas[int(selecao)]["preco"]
preco_total = preco_unitario * int(quantidade)
if entrega.lower() == 's':
    preco_total += 2.99

# Exibir o resumo do pedido
print("\n=== Resumo do Pedido ===")
print(f"Pizza: {menu_de_pizzas[int(selecao)]['nome']}")
print(f"Quantidade: {quantidade}")
if entrega.lower() == 's':
    print("Taxa de entrega: R$2,99")

print(f"Preço total: R${preco_total:.2f}")
print("========================")
