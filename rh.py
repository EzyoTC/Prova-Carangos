# Responsavel pelo projeto: Enzo Henrique Alvarez Silva
# Modulo 4 - RH

funcionarios = []
proximo_id_func = 1

HORAS_NORMAIS_MES = 220   # horas normais por mes


def calcular_inss(salario_bruto):
    if salario_bruto <= 1412.00:
        return salario_bruto * 0.075
    elif salario_bruto <= 2666.68:
        return salario_bruto * 0.09
    elif salario_bruto <= 4000.03:
        return salario_bruto * 0.12
    else:
        return salario_bruto * 0.14


def calcular_irpf(base):
    # base = salario bruto - INSS
    if base <= 2259.20:
        return 0
    elif base <= 2826.65:
        return base * 0.075
    elif base <= 3751.05:
        return base * 0.15
    elif base <= 4664.68:
        return base * 0.225
    else:
        return base * 0.275


def cadastrar_funcionario():
    global proximo_id_func

    print("\n===== Cadastro de funcionario =====")
    nome = input("  Nome completo: ")
    cpf = input("  CPF: ")
    rg = input("  RG: ")
    endereco = input("  Endereco: ")
    telefone = input("  Telefone: ")
    filhos = int(input("  Quantidade de filhos: "))
    cargo = input("  Cargo (ex: operador, gerente, diretor): ").lower()
    valor_hora = float(input("  Valor por hora (R$): "))

    novo = {
        "id":         proximo_id_func,
        "nome":       nome,
        "cpf":        cpf,
        "rg":         rg,
        "endereco":   endereco,
        "telefone":   telefone,
        "filhos":     filhos,
        "cargo":      cargo,
        "valor_hora": valor_hora
    }

    funcionarios.append(novo)
    proximo_id_func += 1
    print(f"[OK]: Funcionario '{nome}' cadastrado com sucesso!")


def listar_funcionarios():
    if len(funcionarios) == 0:
        print("\n[AVISO]: Nenhum funcionario cadastrado.")
        return

    print("\n===== Lista de funcionarios =====")
    for f in funcionarios:
        print(
            f"  ID: {f['id']} | {f['nome']} | "
            f"Cargo: {f['cargo']} | "
            f"Valor/hora: R$ {f['valor_hora']:.2f} | "
            f"Filhos: {f['filhos']}"
        )
    print("=================================\n")


def calcular_salario_funcionario(func, horas_trabalhadas):
    valor_hora = func["valor_hora"]
    cargo      = func["cargo"]

    # horas extras so para quem nao e gerente nem diretor
    if cargo != "gerente" and cargo != "diretor":
        if horas_trabalhadas > HORAS_NORMAIS_MES:
            horas_extras  = horas_trabalhadas - HORAS_NORMAIS_MES
            horas_normais = HORAS_NORMAIS_MES
        else:
            horas_extras  = 0
            horas_normais = horas_trabalhadas
    else:
        horas_extras  = 0
        horas_normais = horas_trabalhadas

    salario_bruto   = (horas_normais * valor_hora) + (horas_extras * valor_hora * 1.5)
    inss            = calcular_inss(salario_bruto)
    base_irpf       = salario_bruto - inss
    irpf            = calcular_irpf(base_irpf)
    salario_liquido = salario_bruto - inss - irpf

    return {
        "horas_normais":   horas_normais,
        "horas_extras":    horas_extras,
        "salario_bruto":   salario_bruto,
        "inss":            inss,
        "irpf":            irpf,
        "salario_liquido": salario_liquido,
        "paga_ir":         irpf > 0
    }


def calcular_salario_menu():
    listar_funcionarios()
    if len(funcionarios) == 0:
        return

    id_func = int(input("  ID do funcionario: "))

    func = None
    for f in funcionarios:
        if f["id"] == id_func:
            func = f
            break

    if func is None:
        print("[ERRO] Funcionario nao encontrado.")
        return

    horas = int(input(f"  Horas trabalhadas no mes ({func['nome']}): "))
    resultado = calcular_salario_funcionario(func, horas)

    print(f"\n  [ CALCULO DE SALARIO - {func['nome'].upper()} ]")
    print(f"  Cargo           : {func['cargo']}")
    print(f"  Horas normais   : {resultado['horas_normais']}")
    print(f"  Horas extras    : {resultado['horas_extras']}")
    print(f"  Salario bruto   : R$ {resultado['salario_bruto']:>10.2f}")
    print(f"  Desconto INSS   : R$ {resultado['inss']:>10.2f}")
    print(f"  Desconto IRPF   : R$ {resultado['irpf']:>10.2f}")
    print(f"  Salario liquido : R$ {resultado['salario_liquido']:>10.2f}")
    print(f"  Paga IR         : {'Sim' if resultado['paga_ir'] else 'Nao'}\n")


def relatorio_rh():
    if len(funcionarios) == 0:
        print("\n[AVISO] Nenhum funcionario cadastrado.")
        return

    print("\nCARANGOS S/A - RELATORIO DE RH")
    print("================================")
    print(f"  {'Nome':<25} {'Cargo':<12} {'Sal. Liquido':>14}  {'Paga IR'}")
    print("  " + "-" * 60)

    for f in funcionarios:
        resultado = calcular_salario_funcionario(f, HORAS_NORMAIS_MES)
        paga_ir = "Sim" if resultado["paga_ir"] else "Nao"
        print(
            f"  {f['nome']:<25} "
            f"{f['cargo']:<12} "
            f"R$ {resultado['salario_liquido']:>10.2f}  "
            f"{paga_ir}"
        )

    print("================================\n")


def menu_rh():
    while True:
        print("\n-- Menu RH --")
        print("  [1] Cadastrar funcionario")
        print("  [2] Listar funcionarios")
        print("  [3] Calcular salario de um funcionario")
        print("  [4] Emitir relatorio de RH")
        print("  [0] Voltar")
        opcao = input("  Escolha: ")

        if opcao == "1":
            cadastrar_funcionario()
        elif opcao == "2":
            listar_funcionarios()
        elif opcao == "3":
            calcular_salario_menu()
        elif opcao == "4":
            relatorio_rh()
        elif opcao == "0":
            break
        else:
            print("[AVISO] Opcao invalida.")


if __name__ == "__main__":
    menu_rh()
