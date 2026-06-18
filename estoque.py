# Responsavel pelo projeto: Enzo Henrique Alvarez Silva
# Modulo 2 - Estoque

produtos = []

proximo_codigo = 1


def buscar_produto_por_codigo(codigo):
    for p in produtos:
        if p["codigo"].upper() == codigo.upper():
            return p
    return None


def buscar_produto_por_nome(nome):
    resultados = []
    for p in produtos:
        if nome.lower() in p["nome"].lower():
            resultados.append(p)
    return resultados


def cadastrar_produto():
    global proximo_codigo

    print("\n===== Cadastro de produto =====")
    codigo = input("  Codigo (ex: P011): ").upper()

    if buscar_produto_por_codigo(codigo):
        print(f"[AVISO] Produto com codigo '{codigo}' ja existe no estoque!")
        return

    nome       = input("  Nome do produto: ")
    fabricacao = input("  Data de fabricacao (dd/mm/aaaa): ")
    fornecedor = input("  Fornecedor: ")
    quantidade = int(input("  Quantidade: "))
    valor      = float(input("  Valor de compra (R$): "))

    novo = {
        "codigo":     codigo,
        "nome":       nome,
        "fabricacao": fabricacao,
        "fornecedor": fornecedor,
        "quantidade": quantidade,
        "valor":      valor
    }

    produtos.append(novo)
    proximo_codigo += 1
    print(f"[OK] Produto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    if len(produtos) == 0:
        print("\n[AVISO] Nenhum produto cadastrado.")
        return

    print("\n===== Lista de produtos =====")
    for p in produtos:
        total = p["quantidade"] * p["valor"]
        print(
            f"  [{p['codigo']}] {p['nome']:<25} | "
            f"Qtd: {p['quantidade']:>5} | "
            f"Valor unit: R${p['valor']:>8.2f} | "
            f"Total: R${total:>10.2f} | "
            f"Fornecedor: {p['fornecedor']}"
        )
    print("=============================\n")


def pesquisar_produto():
    print("\n  [1] Pesquisar por codigo")
    print("  [2] Pesquisar por nome")
    tipo = input("  Escolha: ")

    if tipo == "1":
        codigo = input("  Codigo: ")
        p = buscar_produto_por_codigo(codigo)
        if p:
            total = p["quantidade"] * p["valor"]
            print(f"\n  Encontrado: [{p['codigo']}] {p['nome']}")
            print(f"  Fabricacao : {p['fabricacao']}")
            print(f"  Fornecedor : {p['fornecedor']}")
            print(f"  Quantidade : {p['quantidade']}")
            print(f"  Valor unit : R$ {p['valor']:.2f}")
            print(f"  Total      : R$ {total:.2f}\n")
        else:
            print("[AVISO] Produto nao encontrado.")

    elif tipo == "2":
        nome = input("  Nome (ou parte do nome): ")
        resultados = buscar_produto_por_nome(nome)
        if len(resultados) == 0:
            print("[AVISO] Nenhum produto encontrado com esse nome.")
        else:
            print(f"\n  {len(resultados)} produto(s) encontrado(s):")
            for p in resultados:
                print(f"  [{p['codigo']}] {p['nome']} | Qtd: {p['quantidade']} | R$ {p['valor']:.2f}")
    else:
        print("[AVISO] Opcao invalida.")


def calcular_custos():
    if len(produtos) == 0:
        print("\n[AVISO] Nenhum produto no estoque.")
        return

    total_estoque = 0
    for p in produtos:
        total_estoque += p["quantidade"] * p["valor"]

    # divide o total pelos meses do ano para projetar semanal e mensal
    custo_mensal  = total_estoque / 12
    custo_semanal = custo_mensal / 4
    custo_anual   = total_estoque

    print("\n[ CUSTOS DO ESTOQUE ]")
    print(f"  Valor total em estoque : R$ {total_estoque:>12.2f}")
    print(f"  Custo semanal estimado : R$ {custo_semanal:>12.2f}")
    print(f"  Custo mensal estimado  : R$ {custo_mensal:>12.2f}")
    print(f"  Custo anual estimado   : R$ {custo_anual:>12.2f}\n")


def menu_estoque():
    while True:
        print("\n-- Menu estoque --")
        print("  [1] Listar todos os produtos")
        print("  [2] Cadastrar produto")
        print("  [3] Pesquisar produto")
        print("  [4] Calcular custos do estoque")
        print("  [0] Voltar")
        opcao = input("  Escolha: ")

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            pesquisar_produto()
        elif opcao == "4":
            calcular_custos()
        elif opcao == "0":
            break
        else:
            print("[AVISO] Opcao invalida.")


if __name__ == "__main__":
    menu_estoque()
