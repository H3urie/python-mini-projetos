import os

palavra_secreta = "abacate"
letras_certas = " "
tentativas = 0


print("Nesse jogo, você vai tentar adivinhar a palavra digitando apenas uma letra por vez.\n")

while True:
    
    letra_digitada = input("Digite uma letra: ")
    tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra.\n")
        continue
        
    if letra_digitada in palavra_secreta:
        letras_certas += letra_digitada
        
    palavra_formada = ""
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"

    os.system("cls")

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        print(f"Parabéns, você conseguiu completar a frase!\n Você precisou de '{tentativas}' tentativas")
        break

   


  