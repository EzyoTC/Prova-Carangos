# Responsavel pelo projeto: Enzo Henrique Alvarez Silva
# Menu geral - conecta todos os modulos

import operacional
import estoque
import financeiro
import rh


def exibir_menu_geral():
    print("""
╔══════════════════════════════════════════╗
║         CARANGOS S/A — SISTEMA           ║
╠══════════════════════════════════════════╣
║  [1] Modulo 1 - Operacional              ║
║  [2] Modulo 2 - Estoque                  ║
║  [3] Modulo 3 - Financeiro               ║
║  [4] Modulo 4 - RH                       ║
║  [0] Sair                                ║
╚══════════════════════════════════════════╝
""")


def iniciar():
    print("\nBem-vindo ao sistema da Carangos S/A!")

    while True:
        exibir_menu_geral()
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            operacional.menu_operacional()

        elif opcao == "2":
            estoque.menu_estoque()

        elif opcao == "3":
            financeiro.menu_financeiro()

        elif opcao == "4":
            rh.menu_rh()

        elif opcao == "0":
            print("Encerrando sistema. Ate logo!")
            break

        else:
            print("[AVISO] Opcao invalida. Tente novamente.")


iniciar()
