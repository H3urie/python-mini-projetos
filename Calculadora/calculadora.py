
while True:
    print("-" * 70, "\n Bem vindo a sua calculadora, as funções são as seguintes:\n\n Soma:  + \n Subtração:  - \n multiplicação:  * \n divisão:  / \n", "-" * 70)
    operador = input("\nEscolha um desses operadores lógicos digitando seu respectivo simbolo: ")
    operadores_permitidos = "*+/-"

    if operador not in operadores_permitidos:
       print("O operador que você digitou está incorreto.")

    if operador == "+":
        soma_1 = input("Digite um número: ")
        soma_2 = input("Digite outro numero: ")
        
        try:
          soma_1_int = int(soma_1)
          soma_2_int = int(soma_2)

          result =  soma_1_int + soma_2_int
          print(f"Resultado: {result}")
            
        except:
            print("O contéudo que você digitou não é um numero.")

    if operador == "-":
        sub_1 = input("Digite um número: ")
        sub_2 = input("Digite outro numero: ")
        
        try:
          sub_1_int = int(sub_1)
          sub_2_int = int(sub_2)

          result =  sub_1_int - sub_2_int
          print(f"Resultado: {result}")
            
        except:
            print("O contéudo que você digitou não é um numero.")

    if operador == "*":
        mult_1 = input("Digite um número: ")
        mult_2 = input("Digite outro numero: ")
        
        try:
          mult_1_float = float(mult_1)
          mult_2_float = float(mult_2)

          result =  mult_1_float * mult_2_float
          print(f"Resultado: {result:.2f}")
            
        except:
            print("O contéudo que você digitou não é um numero.")

    if operador == "/":
        div_1 = input("Digite um número: ")
        div_2 = input("Digite outro numero: ")
        
        try:
          div_1_float = float(div_1)
          div_2_float = float(div_2)

          result =  div_1_float / div_2_float
          print(f"Resultado: {result:.2f}")
            
        except:
            print("O contéudo que você digitou não é um numero.")

    
    
    sair = input("Você deseja sair? [s]im ou [n]ão: ").lower()

    if sair == "n" or sair == "nao" or sair == "não":
        continue
    elif sair == "s" or sair == "sim":
        break
