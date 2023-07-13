import os
import time
import sys

#Declaração de variáveis

clientes = []
contas = []
extrato = []
usuario_logado = False
valor_deposito = 0
valor_saque = 0
saques_realizados = 0
saldo = 0
LIMITE_SAQUES = 3

menu_register = """
               ----------------------BANK SYSTEM - ÁREA DO CLIENTE-----------------
                |  Olá. Selecione uma das opções abaixo :                         |
                |                                                                 |
                |  [1] Cadastro do Cliente                                        |
                |  [2] Login do Cliente                                           |
                |  [3] Sair                                                       |  
                |                                                                 |
                -------------------------------------------------------------------
                """


menu_selecao = """
    -------------------------- BANK SYSTEM ----------------------------
    |  Olá. Selecione uma das opções abaixo que você deseja realizar: |
    |                                                                 |
    |  [1] Depósito                                                   |
    |  [2] Saque                                                      |
    |  [3] Extrato                                                    |
    |  [4] Criar nova conta                                           |
    |  [5] Listar contas                                              |
    |  [6] Fazer logoff                                               |
    |                                                                 |
    -------------------------------------------------------------------
    """

def menu_selecao_2(usuario_logado, numero_conta, clientes):
    menu_selecao_opcional = """
    -------------------------- BANK SYSTEM ----------------------------
    |  Olá. Selecione uma das opções abaixo que você deseja realizar: |
    |                                                                 |
    |  [1] Depósito                                                   |
    |  [2] Saque                                                      |
    |  [3] Extrato                                                    |
    |  [4] Criar nova conta                                           |
    |  [5] Listar contas                                              |
    |  [6] Fazer logoff                                               |
    |                                                                 |
    -------------------------------------------------------------------
    """
    print(menu_register)
    opcao_area_cliente = input("Desejo a opção: ")
    os.system("cls")
    if opcao_area_cliente == "1":
        cadastro_cliente(numero_conta, clientes, usuario_logado)
        criar_conta(numero_conta = numero_conta, clientes = clientes, usuario_logado=usuario_logado)
    elif opcao_area_cliente == "2":
        login_usuario(numero_conta, clientes, usuario_logado)

#Declaração de funções
def function_deposito(saldo, valor_deposito, /):
    saldo += valor_deposito
    print("\n""Estamos depositando o valor solicitado. Por favor, aguarde um momento...")
    time.sleep(1.5)
    print(f"""
        O valor foi depositado com sucesso.
        VALOR DEPOSITADO = {valor_deposito:.2f}
        SALDO DA CONTA = {saldo:.2f}
            """)
    extrato.append(f"Depósito realizado: R${valor_deposito:.2f} - SALDO TOTAL:R${saldo:.2f}")
    time.sleep(1.5)
    return saldo

def function_saque(*, saldo, saques_realizados, valor_saque, LIMITE_SAQUES, extrato):
    if saques_realizados < LIMITE_SAQUES:
        if valor_saque <= 500:
            if valor_saque <= saldo:
                saldo -= valor_saque
                print("\n""Estamos fazendo o saque do valor solicitado. Por favor, aguarde um momento...")
                time.sleep(1.5)
                print(f"""
                    O valor foi sacado com sucesso.
                    VALOR SACADO = R${valor_saque:.2f}
                    SALDO DA CONTA = R${saldo:.2f}
                    """)
                saques_realizados += 1
                extrato.append(f"Saque realizado: R${valor_saque:.2f} - SALDO TOTAL:R${saldo:.2f}")
                time.sleep(1.5)
                
            else:
                print("ERRO. Seu saldo é insuficiente para sacar este valor")
                time.sleep(1.5)
                
        else: 
            print("ERRO. O limite máximo para saques é de R$500.00")
            time.sleep(1.5)
           
    else:
        print("ERRO. Você pode realizar somente 3 saques diários")
        time.sleep(1.5)
    return saldo, saques_realizados, extrato
        
def function_extrato(saldo, /, *, extrato):
    menu_extrato = """
            ----------------------------
            |        MENU EXTRATO     |
            ----------------------------
            """
    print(menu_extrato)
    if len(extrato) == 0:
        print("Não foram realizadas movimentações")
        time.sleep(1.5)
    else:
        for i in extrato:
            print(i)
        print(f"""
            SALDO ATUAL DA CONTA:R${saldo:.2f}
            """)
        time.sleep(1.5)
    return saldo, extrato

def cadastro_cliente(numero_conta, clientes, usuario_logado):
    
    menu_cadastro_cliente = """
            ----------------------------------
            |        CADASTRO DO CLIENTE     |
            ----------------------------------
            """
    print(menu_cadastro_cliente)
    cpf = input("Digite seu CPF (Digite somente os números):")
    if cpf in clientes:
        print("ERRO. Já existe um usuário cadastrado com este CPF")
    else:       
        nome = input("Digite seu nome completo:")
        data_nascimento = input("Digite sua data de nascimento (Dia-Mês-Ano):")
        endereco = input("Digite seu endereço (Ex: Logradouro, Número - Bairro - Cidade/Sigla Estado):")
        print("Usuário registrado com sucesso")
        clientes.append({"nome": nome,"cpf":cpf, "data_nascimento": data_nascimento, "endereco": endereco})
        criar_conta(numero_conta, clientes, usuario_logado)
    

def valida_usuario(cpf, clientes):
    for cliente in clientes:
        filtro = [cliente]
        if cliente["cpf"] == cpf:
            if clientes:
                return filtro[0] 
            else:
                return None

def criar_conta(numero_conta, clientes, usuario_logado):
    menu_criar_conta_bancaria = """
            ----------------------------------------------
            |        CRIAR CONTA BANCÁRIA DO CLIENTE     |
            ----------------------------------------------
            """
    print(menu_criar_conta_bancaria)
    cpf = input("Informe o CPF do cliente cadastrado: ")
    cliente = valida_usuario(cpf, clientes)
    if cliente:
        print("Conta criada com sucesso")
        agencia = "0001"
        numero_conta += 1
        contas.append({"agencia":agencia, "numero_conta":numero_conta, "cliente": cliente})
        usuario_logado = True
        print("Estamos te redirecionando para o sistema")
        time.sleep(1.5)
        os.system("cls")
        menu_inicial(usuario_logado, saldo, saques_realizados, extrato)
    else:
        print("")
        print("Para criar uma conta em nosso banco, é necessário fazer o Cadastro do Cliente.")
        print("Por favor, digite o mesmo CPF que foi usado no Cadastro do Cliente")
        usuario_logado = False
        criar_conta(numero_conta, clientes, usuario_logado)




    
def listar_contas(contas):
    for conta in contas:
        text = f""" 
        ======================================================
            Agência: {conta["agencia"]}
            Número da Conta: {conta["numero_conta"]}
            Nome do Titular: {conta["cliente"]["nome"]}
        =====================================================
            """
        print(text)
    time.sleep(1.5)



def login_usuario(numero_conta, clientes, usuario_logado):     
    menu_login_cliente = """
            ----------------------------------
            |        LOGIN DO CLIENTE        |
            ----------------------------------
            """
    print(menu_login_cliente)
    cpf_digitado = input("Digite seu CPF (Digite somente os números):")
    if clientes == []:
        print("Você não é um cliente. Por favor, se cadastre")
        cadastro_cliente(numero_conta, clientes, usuario_logado)
    else:
        for keys in clientes:
            if keys["cpf"] == cpf_digitado:
                usuario_logado = True
                print("Estamos te redirecionando para o sistema")
                time.sleep(1.5)
                os.system("cls")
                menu_inicial(usuario_logado, saldo, saques_realizados, extrato)
            else:
                print("CPF não cadastrado. Cadastre para utilizar nosso sistema")
                time.sleep(3)
                os.system("cls")
                



        
        
def menu_inicial(usuario_logado, saldo, saques_realizados, extrato):
    while usuario_logado == True:
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
                print(f"SALDO ATUAL:R${saldo:.2f}")
                valor_deposito = float(input("Qual valor você deseja depositar em sua conta? => R$"))
                saldo = function_deposito(saldo, valor_deposito)
        
            elif opcao_selecionada == "2":
                menu_saque = """
                ----------------------------
                |        MENU SAQUE    |
                ----------------------------
                """
                print(menu_saque)
                print(f"SALDO ATUAL:R${saldo:.2f}")
                valor_saque = float(input("Qual valor você deseja sacar em sua conta? => R$")) 
                saldo, saques_realizados, extrato = function_saque(saldo=saldo, saques_realizados=saques_realizados, valor_saque=valor_saque, LIMITE_SAQUES=3, extrato=extrato )

            elif opcao_selecionada == "3":
                saldo, extrato = function_extrato(saldo, extrato=extrato)
    
            elif opcao_selecionada == "4":
                numero_conta = (len(contas))
                criar_conta(numero_conta = numero_conta, clientes = clientes, usuario_logado=usuario_logado)

            elif opcao_selecionada == "5":
                listar_contas(contas)

            elif opcao_selecionada == "6":
                usuario_logado = False
                os.system("cls")
                break
    

            else:
                print("Opção inválida. Por favor, selecione uma opção válida")
    while usuario_logado == False:
        numero_conta = (len(contas))
        menu_selecao_2(usuario_logado, numero_conta, clientes)


#Primeira ocorrência do Menu
print(menu_register)
opcao_area_cliente = input("Desejo a opção: ")
os.system("cls")
if opcao_area_cliente == "1":
    numero_conta = (len(contas))
    cadastro_cliente(numero_conta, clientes, usuario_logado)
    criar_conta(numero_conta = 0, clientes = clientes, usuario_logado=usuario_logado)

elif opcao_area_cliente == "2":
    numero_conta = (len(contas))
    login_usuario(numero_conta, clientes, usuario_logado)
    #criar_conta(numero_conta = numero_conta, clientes = clientes, usuario_logado=usuario_logado)
    
elif opcao_area_cliente == "3":
    sys.exit()
else:
    print("Opção inválida. DIgite uma opção válida")




