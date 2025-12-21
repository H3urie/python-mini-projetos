import os

letras_permitidas = "ials"
lista = []

while True:

    
    opções = input("\nSelecione uma opção: \n [i]nserir [a]pagar [l]istar [s]air: ").lower()
    
    if opções not in letras_permitidas:
        print("Digite um dos comandos permitidos.")

    if opções == "i":
        inserir = str(input("Item: "))
        if inserir.isalpha():
            lista.append(inserir)
        else:
            print("Por favor não digite numeros ou caracteres especiais.")
            continue
    
    if opções == "a":
        if bool(lista) is True:
            for indice, valor in enumerate(lista):
                print(f"{indice} - {valor}")
            remover = (input("Digite qual indice você quer remover: "))


            try:
                remover = int(remover)
                del lista[remover]
                print(f"Você removeu o indice {remover} com sucesso.")
            except:
                print("\nNão foi possível apagar este índice")

        else:
            print("Você não tem nenhum valor para apagar.")
            continue
    
    if opções == "l":
        if bool(lista) is True:
            os.system("cls")
            for indice, valor in enumerate(lista):
                print(f"{indice} - {valor}")
        else:
            print("Você não tem itens para ser listados.")

    if opções == "s":
        print("Saindo...")
        break