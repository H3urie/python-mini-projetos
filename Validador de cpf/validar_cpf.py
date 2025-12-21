while True:

    cpf_inteiro = "29700995003"
    cpf = cpf_inteiro[:9]


    cpf_list = list(cpf)
    mult = 10 
    lista_mult = []
    for i, valor in enumerate(cpf_list):
        conta = int(cpf_list[i]) * mult
        mult -= 1
        lista_mult.append(conta)

    soma = 0
    for i, valor in enumerate(lista_mult):
        soma += valor

    resto = soma * 10 % 11
    if resto > 9:
        
        resto = 0
        cpf += str(resto)
    else:
        cpf += str(resto)

    
    cpf_list = list(cpf)
    mult = 11 
    lista_mult = []
    for i, valor in enumerate(cpf_list):
        conta = int(cpf_list[i]) * mult
        mult -= 1
        lista_mult.append(conta)

    soma = 0
    for i, valor in enumerate(lista_mult):
        soma += valor

    resto = soma * 10 % 11
    if resto > 9:
        
        resto = 0
        cpf += str(resto)
    else:
        cpf += str(resto)
        
    if cpf == cpf_inteiro:
        print(f"O CPF: {cpf} é valido")
    else:
        print("CPF INVALIDO")
        
    break

    

