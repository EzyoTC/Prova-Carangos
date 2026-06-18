# Responsavel pelo projeto: Enzo Henrique Alvarez Silva
# Modulo 3 - Financeiro

despesas = {}
total_carros_produzidos = 0


def cadastrar_despesas():
    global despesas, total_carros_produzidos

    print("\n===== Cadastro de despesas fixas =====")
    agua      = float(input("  Agua (R$): "))
    luz       = float(input("  Luz (R$): "))
    salarios  = float(input("  Salarios (R$): "))
    impostos  = float(input("  Impostos (R$): "))

    despesas = {
        "agua":     agua,
        "luz":      luz,
        "salarios": salarios,
        "impostos": impostos
    }

    total_carros_produzidos = int(input("  Total de carros produzidos no mes: "))
    print("[OK]: Despesas cadastradas com sucesso!")


def calcular_total_despesas():
    total = 0
    for chave in despesas:
        total += despesas[chave]
    return total


def calcular_custo_por_carro():
    if total_carros_produzidos == 0:
        return 0
    return calcular_total_despesas() / total_carros_produzidos


def calcular_preco_venda():
    custo = calcular_custo_por_carro()
    return custo * 1.5


def relatorio_financeiro():
    if len(despesas) == 0:
        print("\n[AVISO]: Nenhuma despesa cadastrada ainda.")
        return

    total       = calcular_total_despesas()
    custo_carro = calcular_custo_por_carro()
    preco_venda = calcular_preco_venda()

    print("\nCARANGOS S/A - RELATORIO FINANCEIRO")
    print("=====================================")
    print("\nDESPESAS FIXAS:")
    print(f"  Agua            : R$ {despesas['agua']:>10.2f}")
    print(f"  Luz             : R$ {despesas['luz']:>10.2f}")
    print(f"  Salarios        : R$ {despesas['salarios']:>10.2f}")
    print(f"  Impostos        : R$ {despesas['impostos']:>10.2f}")
    print(f"  Total           : R$ {total:>10.2f}")

    print(f"\nCALCULO POR CARRO: ")
    print(f"  Carros produzidos  : {total_carros_produzidos}")
    print(f"  Custo por carro    : R$ {custo_carro:>10.2f}")
    print(f"  Preco de venda     : R$ {preco_venda:>10.2f}  (50% de lucro)")
    print(f"  Lucro por carro    : R$ {preco_venda - custo_carro:>10.2f}")
    print("=====================================\n")


def menu_financeiro():
    while True:
        print("\n-- Menu financeiro --")
        print("  [1] Cadastrar despesas")
        print("  [2] Ver relatorio financeiro")
        print("  [0] Voltar")
        opcao = input("  Escolha: ")

        if opcao == "1":
            cadastrar_despesas()
        elif opcao == "2":
            relatorio_financeiro()
        elif opcao == "0":
            break
        else:
            print("[AVISO]: Opcao invalida.")


if __name__ == "__main__":
    menu_financeiro()
