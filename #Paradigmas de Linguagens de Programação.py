#Paradigmas de Linguagens de Programação


class Item:
    def calcular_total(item):
        return item.valor + item.acrescimo - item.desconto

    def calcular_acrescimo(item, valor_acrescimo):
        item.acrescimo += valor_acrescimo

    def calcular_desconto(item, valor_desconto):
        item.desconto += valor_desconto

    def mostrar_informacoes(item):
        total = item.calcular_total()
        print(f"Produto: {item.descricao}")
        print(f"Preço: R$ {item.valor:.2f}")
        print(f"Acréscimo: R$ {item.acrescimo:.2f}")
        print(f"Desconto: R$ {item.desconto:.2f}")
        print(f"Total: R$ {total:.2f}")
        print("-----------")


class Carrinho:
    def adicionar_item(carrinho, item):
        carrinho.itens.append(item)

    def acrescimo_item(carrinho, codigo, valor_acrescimo):
        for item in carrinho.itens:
            if item.codigo == codigo:
                item.calcular_acrescimo(valor_acrescimo)

    def desconto_item(carrinho, codigo, valor_desconto):
        for item in carrinho.itens:
            if item.codigo == codigo:
                item.calcular_desconto(valor_desconto)

    def adicionar_acrescimo_total(carrinho, valor_acrescimo_total):
        num_itens = len(carrinho.itens)
        if num_itens > 0:
            valor_acrescimo_individual = valor_acrescimo_total / num_itens
            for item in carrinho.itens:
                item.calcular_acrescimo(valor_acrescimo_individual)

    def aplicar_desconto_total(carrinho, valor_desconto_total):
        num_itens = len(carrinho.itens)
        if num_itens > 0:
            valor_desconto_individual = valor_desconto_total / num_itens
            for item in carrinho.itens:
                item.calcular_desconto(valor_desconto_individual)

    def finalizar_compra(carrinho):
        print("\nItens do Carrinho:")
        for item in carrinho.itens:
            item.mostrar_informacoes()

        desconto_total = sum(item.desconto for item in carrinho.itens)
        acrescimo_total = sum(item.acrescimo for item in carrinho.itens)
        valor_total = sum(item.calcular_total() for item in carrinho.itens)

        print(f"Desconto Total: R$ {desconto_total:.2f}")
        print(f"Acréscimo Total: R$ {acrescimo_total:.2f}")
        print(f"Valor Total: R$ {valor_total:.2f}")


carrinho = Carrinho()
itens = []

while True:
    print("Sistema de controle de desconto / acréscimos para itens de carrinho")
    print("\nMenu:")
    print("1. Inserir item ao carrinho")
    print("2. Acrescentar valor ao Item")
    print("3. Descontar valor ao Item")
    print("4. Acrescentar valor a Total aos itens")
    print("5. Aplicar desconto a total aos itens")
    print("6. Finalizar procedimento")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        codigo = input("Código do produto: ")
        descricao = input("Descrição do produto: ")
        valor = float(input("Preço do produto: "))
        item = Item()
        item.codigo = codigo
        item.descricao = descricao
        item.valor = valor
        itens.append(item)
        carrinho.itens = itens
    elif escolha == '2':
        codigo = input("Código do produto: ")
        valor_acrescimo = float(input("Valor do acréscimo: "))
        carrinho.acrescimo_item(codigo, valor_acrescimo)
    elif escolha == '3':
        codigo = input("Código do produto: ")
        valor_desconto = float(input("Valor do desconto: "))
        carrinho.desconto_item(codigo, valor_desconto)
    elif escolha == '4':
        valor_acrescimo_total = float(input("Valor do acréscimo total: "))
        carrinho.adicionar_acrescimo_total(valor_acrescimo_total)
    elif escolha == '5':
        valor_desconto_total = float(input("Valor do desconto total: "))
        carrinho.aplicar_desconto_total(valor_desconto_total)
    elif escolha == '6':
        carrinho.finalizar_compra()
        break
    else:
        print("Opção inválida. Tente novamente.")
