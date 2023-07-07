import os
import time

menu_selecao = """
-------------------------- BANK SYSTEM ----------------------------
|  Olá. Selecione uma das opções abaixo que você deseja realizar: |
|                                                                 |
|  [1] Depósito                                                   |
|  [2] Saque                                                      |
|  [3] Extrato                                                    |
|  [4] Sair                                                       |
|                                                                 |
-------------------------------------------------------------------
"""

valor_deposito = 0
valor_saque = 0
saques_realizados = 0
extrato = []
saldo = 0
LIMITE_SAQUES = 3

while True:
    print(menu_selecao)
    opcao_selecionada = input("Desejo a opção: ")
    os.system("cls")
    if opcao_selecionada == "1":
        menu_deposito = """
            ----------------------------
            |        MENU DEPÓSITO     |
            ----------------------------
            """
        print(menu_deposito)
        print(f"SALDO ATUAL:R${saldo}")
        valor_deposito = float(input("Qual valor você deseja depositar em sua conta? => R$"))
        saldo += valor_deposito
        print("\n""Estamos depositando o valor solicitado. Por favor, aguarde um momento...")
        time.sleep(1.5)
        print(f"""
            O valor foi depositado com sucesso.
            VALOR DEPOSITADO = R${valor_deposito}
            SALDO DA CONTA = R${saldo}
              """)
        extrato.append(f"Depósito realizado: R${valor_deposito} - SALDO TOTAL:R${saldo}")
        time.sleep(3)
        
    elif opcao_selecionada == "2": 
        menu_saque = """
            ----------------------------
            |        MENU SAQUE    |
            ----------------------------
            """
        print(menu_saque)
        print(f"SALDO ATUAL:R${saldo}")
        valor_saque = float(input("Qual valor você deseja sacar em sua conta? => R$"))
        if saques_realizados < LIMITE_SAQUES:
            if valor_saque <= 500:
                if valor_saque <= saldo:
                    saldo -= valor_saque
                    print("\n""Estamos fazendo o saque do valor solicitado. Por favor, aguarde um momento...")
                    time.sleep(1.5)
                    print(f"""
                        O valor foi sacado com sucesso.
                        VALOR SACADO = R${valor_saque}
                        SALDO DA CONTA = R${saldo}
                        """)
                    saques_realizados += 1
                    extrato.append(f"Saque realizado: R${valor_saque} - SALDO TOTAL:R${saldo}")
                    time.sleep(3)
                else:
                    print("ERRO. Seu saldo é insuficiente para sacar este valor")
                    time.sleep(3)
            else: 
                print("ERRO. O limite máximo para saques é de R$500.00")
                time.sleep(3)
        else:
            print("ERRO. Você pode realizar somente 3 saques diários")
            time.sleep(3)

    elif opcao_selecionada == "3":
        menu_extrato = """
            ----------------------------
            |        MENU EXTRATO     |
            ----------------------------
            """
        print(menu_extrato)
        if len(extrato) == 0:
            print("Não foram realizadas movimentações")
            time.sleep(3)

        else:
            for i in extrato:
                print(i)
            print(f"""
                  SALDO ATUAL DA CONTA:R${saldo}
                  """)
            time.sleep(3)

    elif opcao_selecionada == "4":
        break

    else:
        print("Opção inválida. Por favor, selecione uma opção válida")



           




