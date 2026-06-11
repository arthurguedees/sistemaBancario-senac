#Questão 1
clientes = {}
def cadastrar_cliente():
    print("\n=== CADASTRAR CLIENTE ===")
    while True:
        tipo = input("Tipo de pessoa (F - Física / J - Jurídica): ").upper()
        if tipo in ["F", "J"]:
            break
        print("Erro! Digite apenas F ou J.")
    while True:
        nome = input("Nome: ")
        if (nome) >= 3:
            break
        print("Erro! O nome deve ter pelo menos 3 caracteres.")

    if tipo == "F":
        while True:
            documento = input("CPF (com símbolos): ")
            if documento not in clientes:
                break
            print("CPF já cadastrado!")
    else:
        while True:
            documento = input("CNPJ: ")
            if documento not in clientes:
               break
            print("CNPJ já cadastrado!")
    rg = input("RG: ")
    nascimento = input("Data de nascimento: ")
    while True:
        email = input("E-mail: ")
        if "@" in email and "." in email:
            break
        print("E-mail inválido!")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")
    numero = input("Número do imóvel: ")
    cep = input("CEP: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    complemento = input("Complemento: ")
    senha = input("Crie uma senha: ")
    clientes[documento] = {
        "tipo": tipo,
        "nome": nome,
        "documento": documento,
        "rg": rg,
        "nascimento": nascimento,
        "email": email,
        "telefone": telefone,
        "endereco": endereco,
        "numero": numero,
        "cep": cep,
        "cidade": cidade,
        "estado": estado,
        "complemento": complemento,
        "senha": senha,
        "score": 2000,
        "saldo": 0.0
    }
    print("Cliente cadastrado com sucesso!")
def depositar():
    print("\n=== DEPÓSITO ===")
    documento = input("CPF/CNPJ: ")
    if documento not in clientes:
        print("Cliente não encontrado!")
        return
    try:
        valor = float(input("Valor do depósito: R$ "))
        if valor <= 0:
            print("Valor inválido!")
            return
        clientes[documento]["saldo"] += valor
        if valor > 10000:
            clientes[documento]["score"] += 1000
            print("Score aumentado em 1000 pontos!")
        print("Depósito realizado com sucesso!")
    except ValueError:
        print("Digite apenas números!")
def sacar():
    print("\n=== SAQUE ===")
    documento = input("CPF/CNPJ: ")
    if documento not in clientes:
        print("Cliente não encontrado!")
        return
    senha = input("Senha: ")
    if senha != clientes[documento]["senha"]:
        print("Senha incorreta!")
        return
    try:
        valor = float(input("Valor do saque: R$ "))
        if valor <= 0:
            print("Valor inválido!")
            return
        if valor > clientes[documento]["saldo"]:
            print("Saldo insuficiente!")
            return
        clientes[documento]["saldo"] -= valor
        print("Saque realizado com sucesso!")
    except ValueError:
        print("Digite apenas números!")
def consultar_saldo():
    print("\n=== CONSULTAR SALDO ===")
    documento = input("CPF/CNPJ: ")
    if documento not in clientes:
        print("Cliente não encontrado!")
        return
    senha = input("Senha: ")
    if senha != clientes[documento]["senha"]:
        print("Senha incorreta!")
        return
    print(f"Cliente: {clientes[documento]['nome']}")
    print(f"Saldo: R$ {clientes[documento]['saldo']:.2f}")
    print(f"Score: {clientes[documento]['score']}")
def alterar_senha():
    print("\n=== ALTERAR SENHA ===")
    documento = input("CPF/CNPJ: ")
    if documento not in clientes:
        print("Cliente não encontrado!")
        return
    senha_atual = input("Senha atual: ")
    if senha_atual != clientes[documento]["senha"]:
        print("Senha incorreta!")
        return
    nova_senha = input("Nova senha: ")
    clientes[documento]["senha"] = nova_senha
    print("Senha alterada com sucesso!")
while True:
    print("\n===== SISTEMA BANCÁRIO =====")
    print("1 - Cadastrar Cliente")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Consultar Saldo")
    print("5 - Alterar Senha")
    print("0 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar_cliente()
        elif opcao == 2:
            depositar()
        elif opcao == 3:
            sacar()
        elif opcao == 4:
            consultar_saldo()
        elif opcao == 5:
            alterar_senha()
        elif opcao == 0:
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Digite apenas números!")