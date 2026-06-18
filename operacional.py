# Responsavel pelo projeto: Enzo Henrique Alvarez Silva

# modulo operacional
producao_semanal = []
dias_da_semana = ["Segunda-feira", "Terca-feira", "Quarta-feira",
                  "Quinta-feira", "Sexta-feira", "Sabado", "Domingo"]


def cadastrar_producao():
    global producao_semanal
    producao_semanal = []

    print("\n===== Cadastro de producao semanal =====")
    print("Informe a producao (em unidades) de cada turno por dia.")
    print("Digite 0 se o turno nao funcionou naquele dia.\n")

    for i in range(7):
        print(f"--- {dias_da_semana[i]} ---")
        manha = int(input("  Turno manha:  "))
        tarde = int(input("  Turno tarde:  "))
        noite = int(input("  Turno noite:  "))

        dia = {
            "dia": dias_da_semana[i],
            "manha": manha,
            "tarde": tarde,
            "noite": noite,
            "total_dia": manha + tarde + noite
        }

        producao_semanal.append(dia)
        print(f"  Total do dia: {dia['total_dia']} unidades\n")

    print("[OK] Producao semanal cadastrada com sucesso!")


def calc_total_semanal():
    total = 0
    for dia in producao_semanal:
        total += dia["total_dia"]
    return total

def calc_media_diaria():
    return calc_total_semanal() / 7

def calc_total_por_turno(turno):
    total = 0
    for dia in producao_semanal:
        total += dia[turno]
    return total

def calc_media_por_turno(turno):
    return calc_total_por_turno(turno) / 7

def calc_producao_mensal():
    return calc_media_diaria() * 30

def calc_producao_anual():
    return calc_producao_mensal() * 12

def calc_producao_ideal():
    cap_2_turnos = 500
    cap_3_turnos = 500 * 1.5
    return {
        "mensal_2_turnos": cap_2_turnos,
        "mensal_3_turnos": cap_3_turnos,
        "anual_2_turnos":  cap_2_turnos * 12,
        "anual_3_turnos":  cap_3_turnos * 12
    }


def emitir_relatorio():
    if len(producao_semanal) == 0:
        print("\n[AVISO] Nenhuma producao cadastrada. Cadastre a semana primeiro.")
        return

    total_semanal = calc_total_semanal()
    media_diaria  = calc_media_diaria()
    total_manha   = calc_total_por_turno("manha")
    total_tarde   = calc_total_por_turno("tarde")
    total_noite   = calc_total_por_turno("noite")
    media_manha   = calc_media_por_turno("manha")
    media_tarde   = calc_media_por_turno("tarde")
    media_noite   = calc_media_por_turno("noite")
    prod_mensal   = calc_producao_mensal()
    prod_anual    = calc_producao_anual()
    ideal         = calc_producao_ideal()

    eficiencia_mensal = (prod_mensal / ideal["mensal_3_turnos"]) * 100
    eficiencia_anual  = (prod_anual  / ideal["anual_3_turnos"])  * 100

    print("\nCARANGOS S/A - RELATORIO OPERACIONAL")
    print("======================================")

    print("\n[ PRODUÇÃO DIÁRIA ]")
    for dia in producao_semanal:
        print(
            f"  {dia['dia']:<16} | "
            f"Manha: {dia['manha']:>5}  "
            f"Tarde: {dia['tarde']:>5}  "
            f"Noite: {dia['noite']:>5}  "
            f"Total: {dia['total_dia']:>6}"
        )

    print(f"\n[ RESUMO SEMANAL ]")
    print(f"  Total na semana  : {total_semanal:>8.0f} unidades")
    print(f"  Media por dia    : {media_diaria:>8.1f} unidades")

    print(f"\n[ PRODUÇÃO POR TURNO ]")
    print(f"  Manha  - Total: {total_manha:>6.0f} un  |  Media/dia: {media_manha:>6.1f} un")
    print(f"  Tarde  - Total: {total_tarde:>6.0f} un  |  Media/dia: {media_tarde:>6.1f} un")
    print(f"  Noite  - Total: {total_noite:>6.0f} un  |  Media/dia: {media_noite:>6.1f} un")

    print(f"\n[ PROJEÇÃO ]")
    print(f"  produção mensal estimada : {prod_mensal:>8.0f} unidades")
    print(f"  produção anual estimada  : {prod_anual:>8.0f} unidades")

    print(f"\n[ CAPACIDADE IDEAL (100%) ]")
    print(f"  Com 2 turnos: {ideal['mensal_2_turnos']:>6.0f} un/mes  |  {ideal['anual_2_turnos']:>7.0f} un/ano")
    print(f"  Com 3 turnos: {ideal['mensal_3_turnos']:>6.0f} un/mes  |  {ideal['anual_3_turnos']:>7.0f} un/ano")
    print(f"  (3 turno acrescenta 50% sobre a capacidade de 2 turnos)")

    print(f"\n[ COMPARAÇÃO REAL x IDEAL (3 TURNOS) ]")
    print(f"  produção mensal real     : {prod_mensal:>8.0f} un")
    print(f"  Capacidade mensal ideal  : {ideal['mensal_3_turnos']:>8.0f} un")
    print(f"  Eficiencia mensal        : {eficiencia_mensal:>7.1f}%")
    print(f"\n  produção anual real      : {prod_anual:>8.0f} un")
    print(f"  Capacidade anual ideal   : {ideal['anual_3_turnos']:>8.0f} un")
    print(f"  Eficiencia anual         : {eficiencia_anual:>7.1f}%")

    print("\n[ DIAGNOSTICO ]")
    if eficiencia_mensal >= 90:
        print("  Situacao: OTIMA - produção muito proxima da capacidade maxima.")
    elif eficiencia_mensal >= 70:
        print("  Situacao: BOA - produção satisfatoria, mas ha margem pra crescer.")
    elif eficiencia_mensal >= 50:
        print("  Situacao: REGULAR - menos da metade da capacidade esta sendo usada.")
    else:
        print("  Situacao: CRITICA - produção muito abaixo do potencial da fabrica.")

    print("======================================\n")


def ver_producao_cadastrada():
    if len(producao_semanal) == 0:
        print("\n[AVISO] Nenhuma produção cadastrada ainda.")
        return

    print("\n===== Produção cadastrada =====")
    for dia in producao_semanal:
        print(
            f"  {dia['dia']:<16} | "
            f"Manha: {dia['manha']:>5}  "
            f"Tarde: {dia['tarde']:>5}  "
            f"Noite: {dia['noite']:>5}  "
            f"Total: {dia['total_dia']:>6}"
        )
    print("================================\n")


def menu_operacional():
    while True:
        print("\n-- Menu operacional --")
        print("  [1] Cadastrar producao da semana")
        print("  [2] Ver producao cadastrada")
        print("  [3] Emitir relatorio")
        print("  [0] Voltar")
        opcao = input("  Escolha: ")

        if opcao == "1":
            cadastrar_producao()
        elif opcao == "2":
            ver_producao_cadastrada()
        elif opcao == "3":
            emitir_relatorio()
        elif opcao == "0":
            break
        else:
            print("[AVISO] Opcao invalida.")


if __name__ == "__main__":
    menu_operacional()
