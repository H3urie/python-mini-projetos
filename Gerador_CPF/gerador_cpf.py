import random
cpf_inteiro = ""

while True:

    for i in range(9):
        cpf_inteiro += str(random.randint(0, 9))


    cpf_list = list(cpf_inteiro)
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
        cpf_inteiro += str(resto)
    else:
        cpf_inteiro += str(resto)

    
    cpf_list = list(cpf_inteiro)
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
        cpf_inteiro += str(resto)
    else:
        cpf_inteiro += str(resto)
        
    print(cpf_inteiro)

    break