def validarCelular():
    validar = input("Voce deseja validar seu celular").lower.stip()
    if validar == "sim" or validar == "s":
        print("celular válidado com sucesso")
    else:
        print("autorização bloqueada")
    