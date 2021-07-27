import random


def forca_vazia():
    print("==============")
    print("||")
    print("||")
    print("||")
    print("||")
    print("||")
    print("_________________")


def erro_01():
    print("==============")
    print("||     (oo)")
    print("||")
    print("||")
    print("||")
    print("||")
    print("_________________")


def erro_02():
    print("==============")
    print("||     (oo)")
    print("||      ||")
    print("||      ||")
    print("||")
    print("||")
    print("_________________")


def erro_03():
    print("==============")
    print("||     (oo)")
    print("||      ||===")
    print("||      ||   ")
    print("||")
    print("||")
    print("_________________")


def erro_04():
    print("==============")
    print("||     (oo)")
    print("||   ===||===")
    print("||      ||")
    print("||")
    print("||")
    print("_________________")


def erro_05():
    print("==============")
    print("||     (oo)")
    print("||   ===||===")
    print("||      ||")
    print("||     MW ")
    print("||    MW")
    print("_________________")


def erro_06():
    print("==============")
    print("||     (oo)")
    print("||   ===||===")
    print("||      ||")
    print("||     MWWM")
    print("||    MW  WM")
    print("_________________")
    print()
    print("VOCÊ PERDEU!!")
    print(f"A palavra correta era {escolha}")


def erraLetraTexto():
    print()
    print("===============")
    print("ERROU A LETRA!!")
    print("===============")
    print()


def erro(erro):  # Função que trabalha todos os erros e apresenta a forca e os desenhos
    if erro == 1:
        erro_01()
        for p in palavra:
            print(f"{p}", end=" ")
    elif erro == 2:
        erro_02()
        for p in palavra:
            print(f"{p}", end=" ")
    elif erro == 3:
        erro_03()
        for p in palavra:
            print(f"{p}", end=" ")
    elif erro == 4:
        erro_04()
        for p in palavra:
            print(f"{p}", end=" ")
    elif erro == 5:
        erro_05()
        for p in palavra:
            print(f"{p}", end=" ")
    elif erro == 6:
        erro_06()

    print()


def venceu():
    print("          OO")
    print("        ******")
    print("      **********")
    print("    **************")
    print(" ********************")
    print("PARABÉNS, VOCÊ ACERTOU!!!")
    print(" ********************")
    print("    **************")
    print("      **********")
    print("        ******")
    print("          OO")


# Lista dos nomes
lista_dos_nomes = ["TIBET", "NEUTRON", "URANO", "EINSTEIN", "ALECRIM", "BAHIA", "COQUEIRO"]
lista_letras = []
# Escolhe um dos nomes na lista por sorteio
escolha = random.choice(lista_dos_nomes).upper().strip()


if escolha == "TIBET":
    print("DICA: País do centro asiático")
    palavra = ["_", "_", "_", "_", "_"]
    for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
    print()
    erroMsg = 0
    while palavra != ["T", "I", "B", "E", "T"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()  # Independente se o suário digitar maiúsculo ou minúsculos, o upper() deixa tudo em maiúsculo como na lista principal e o strip para tirar o espaços caso alguém digite um.
        if letra in lista_letras: # Avisar ao usuário que a letra já foi dita!
            print(f"A letra {letra} já saiu, escolha novamente")
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "T":
            palavra[0] = letra
            palavra[4] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "I":
            palavra[1] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "B":
            palavra[2] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[3] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "T" or letra != "I" or letra != "B" or letra != "E":
            erraLetraTexto() # Função para alertar que o usuário errou a letra
            erroMsg = erroMsg + 1
            erro(erroMsg) # Função que trabalha todos os erros e apresenta a forca e os desenhos
            if erroMsg == 6:
                break
elif escolha == "NEUTRON":
    print("DICA: Partícula subatômica")
    palavra = ["_", "_", "_", "_", "_", "_", "_"]
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["N", "E", "U", "T", "R", "O", "N"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra in lista_letras:
            print(f"A letra {letra} já saiu, escolha novamente")
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "N":
            palavra[0] = letra
            palavra[6] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[1] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "U":
            palavra[2] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "T":
            palavra[3] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[4] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "O":
            palavra[5] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "N" or letra != "E" or letra != "B" or letra != "E":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "URANO":
    print("DICA: Planeta do Sistema Solar")
    palavra = ["_", "_", "_", "_", "_"]
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["U", "R", "A", "N", "O"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra in lista_letras:
            print(f"A letra {letra} já saiu, escolha novamente")
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "U":
            palavra[0] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[1] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "A":
            palavra[2] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "N":
            palavra[3] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "O":
            palavra[4] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "U" or letra != "R" or letra != "A" or letra != "N" or letra != "O":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "EINSTEIN":
    print("DICA: Importante nome da física clássica")
    palavra = ["_", "_", "_", "_", "_", "_", "_", "_"]
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["E", "I", "N", "S", "T", "E", "I", "N"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra in lista_letras:
            print(f"A letra {letra} já saiu, escolha novamente")
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "E":
            palavra[0] = letra
            palavra[5] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[1] = letra
            palavra[6] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "N":
            palavra[2] = letra
            palavra[7] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "T":
            palavra[4] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "S":
            palavra[3] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "E" or letra != "I" or letra != "N" or letra != "S" or letra != "T":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "ALECRIM":
    print("DICA: Erva aromática")
    palavra = ["_", "_", "_", "_", "_", "_", "_"]
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["A", "L", "E", "C", "R", "I", "M"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra in lista_letras:
            print(f"A letra {letra} já saiu, escolha novamente")
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "A":
            palavra[0] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "L":
            palavra[1] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[2] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "C":
            palavra[3] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[4] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[5] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "M":
            palavra[6] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "A" or letra != "L" or letra != "E" or letra != "C" or letra != "R" or letra != "I" or letra != "M":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "BAHIA":
    print("DICA: Time de futebol que já foi campeão Brasileiro")
    palavra = ["_", "_", "_", "_", "_"]
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["B", "A", "H", "I", "A"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra in lista_letras:
            print(f"A letra {letra} já saiu, escolha novamente")
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "B":
            palavra[0] = letra
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "A":
            palavra[1] = letra
            palavra[4] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "H":
            palavra[2] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[3] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "B" or letra != "A" or letra != "H" or letra != "I":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "COQUEIRO":
    print("DICA: Árvore do litoral brasileiro de origem asiática")
    palavra = ["_", "_", "_", "_", "_", "_", "_", "_"]
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["C", "O", "Q", "U", "E", "I", "R", "O"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra in lista_letras:
            print(f"A letra {letra} já saiu, escolha novamente")
            for p in palavra: print(f"{p}", end=" ") # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "C":
            palavra[0] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "O":
            palavra[1] = letra
            palavra[7] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "Q":
            palavra[2] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "U":
            palavra[3] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[4] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[5] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[6] = letra
            lista_letras.append(letra)
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "C" or letra != "O" or letra != "Q" or letra != "U" or letra != "E" or letra != "I" or letra != "R":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break

print("+++++++++++++++++++++++++")
print("OBRIGADO E VOLTE SEMPRE!!")
print("+++++++++++++++++++++++++")