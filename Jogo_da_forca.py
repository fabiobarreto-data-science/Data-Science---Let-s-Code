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
    print("VOCÊ PERDEU!!")


# Lista dos nomes
lista_dos_nomes = ["TIBET", "NEUTRON", "URANO", "EINSTEIN", "ALECRIM", "BAHIA", "COQUEIRO"]


escolha = random.choice(lista_dos_nomes).upper().strip()

if escolha == "TIBET":
    print("DICA: País do centro asiático")
    palavra = ["_", "_", "_", "_", "_"]
    erro = 0
    while palavra != ["T", "I", "B", "E", "T"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra == "T":
            palavra[0] = letra
            palavra[4] = letra
            print(palavra)
        elif letra == "I":
            palavra[1] = letra
            print(palavra)
        elif letra == "B":
            palavra[2] = letra
            print(palavra)
        elif letra == "E":
            palavra[3] = letra
            print(palavra)
        elif letra != "T" or letra != "I" or letra != "B" or letra != "E":
            print("ERROU A LETRA!!")
            erro = erro + 1
            if erro == 1:
                erro_01()
            elif erro == 2:
                erro_02()
            elif erro == 3:
                erro_03()
            elif erro == 4:
                erro_04()
            elif erro == 5:
                erro_05()
            elif erro == 6:
                erro_06()
                break
        elif palavra == ["T", "I", "B", "E", "T"]:
            print(palavra)
            break
elif escolha == "NEUTRON":
    print("DICA: Partícula subatômica")
    palavra = ["_", "_", "_", "_", "_", "_", "_"]
    erro = 0
    while palavra != ["N", "E", "U", "T", "R", "O", "N"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra == "N":
            palavra[0] = letra
            palavra[6] = letra
            print(palavra)
        elif letra == "E":
            palavra[1] = letra
            print(palavra)
        elif letra == "U":
            palavra[2] = letra
            print(palavra)
        elif letra == "T":
            palavra[3] = letra
            print(palavra)
        elif letra == "R":
            palavra[4] = letra
            print(palavra)
        elif letra == "O":
            palavra[5] = letra
            print(palavra)
        elif letra != "N" or letra != "E" or letra != "B" or letra != "E":
            print("ERROU A LETRA!!")
            erro = erro + 1
            if erro == 1:
                erro_01()
            elif erro == 2:
                erro_02()
            elif erro == 3:
                erro_03()
            elif erro == 4:
                erro_04()
            elif erro == 5:
                erro_05()
            elif erro == 6:
                erro_06()
                break
        elif palavra == ["N", "E", "U", "T", "R", "O", "N"]:
            print(palavra)
            break
elif escolha == "URANO":
    print("DICA: Planeta do Sistema Solar")
    palavra = ["_", "_", "_", "_", "_"]
    erro = 0
    while palavra != ["U", "R", "A", "N", "O"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra == "U":
            palavra[0] = letra
            print(palavra)
        elif letra == "R":
            palavra[1] = letra
            print(palavra)
        elif letra == "A":
            palavra[2] = letra
            print(palavra)
        elif letra == "N":
            palavra[3] = letra
            print(palavra)
        elif letra == "O":
            palavra[4] = letra
            print(palavra)
        elif letra != "U" or letra != "R" or letra != "A" or letra != "N" or letra != "O":
            print("ERROU A LETRA!!")
            erro = erro + 1
            if erro == 1:
                erro_01()
            elif erro == 2:
                erro_02()
            elif erro == 3:
                erro_03()
            elif erro == 4:
                erro_04()
            elif erro == 5:
                erro_05()
            elif erro == 6:
                erro_06()
                break
        elif palavra == ["U", "R", "A", "N", "O"]:
            print(palavra)
            break
elif escolha == "EINSTEIN":
    print("DICA: Importante Físico clássico")
    palavra = ["_", "_", "_", "_", "_", "_", "_", "_"]
    erro = 0
    while palavra != ["E", "I", "N", "S", "T", "E", "I", "N"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra == "E":
            palavra[0] = letra
            palavra[5] = letra
            print(palavra)
        elif letra == "I":
            palavra[1] = letra
            palavra[6] = letra
            print(palavra)
        elif letra == "N":
            palavra[2] = letra
            palavra[7] = letra
            print(palavra)
        elif letra == "T":
            palavra[4] = letra
            print(palavra)
        elif letra == "S":
            palavra[3] = letra
            print(palavra)
        elif letra != "E" or letra != "I" or letra != "N" or letra != "S" or letra != "T":
            print("ERROU A LETRA!!")
            erro = erro + 1
            if erro == 1:
                erro_01()
            elif erro == 2:
                erro_02()
            elif erro == 3:
                erro_03()
            elif erro == 4:
                erro_04()
            elif erro == 5:
                erro_05()
            elif erro == 6:
                erro_06()
                break
        elif palavra == ["E", "I", "N", "S", "T", "E", "I", "N"]:
            print(palavra)
            break
elif escolha == "ALECRIM":
    print("DICA: Erva aromática")
    palavra = ["_", "_", "_", "_", "_", "_", "_"]
    erro = 0
    while palavra != ["A", "L", "E", "C", "R", "I", "M"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra == "A":
            palavra[0] = letra
            print(palavra)
        elif letra == "L":
            palavra[1] = letra
            print(palavra)
        elif letra == "E":
            palavra[2] = letra
            print(palavra)
        elif letra == "C":
            palavra[3] = letra
            print(palavra)
        elif letra == "R":
            palavra[4] = letra
            print(palavra)
        elif letra == "I":
            palavra[5] = letra
            print(palavra)
        elif letra == "M":
            palavra[6] = letra
            print(palavra)
        elif letra != "A" or letra != "L" or letra != "E" or letra != "C" or letra != "R" or letra != "I" or letra != "M":
            print("ERROU A LETRA!!")
            erro = erro + 1
            if erro == 1:
                erro_01()
            elif erro == 2:
                erro_02()
            elif erro == 3:
                erro_03()
            elif erro == 4:
                erro_04()
            elif erro == 5:
                erro_05()
            elif erro == 6:
                erro_06()
                break
        elif palavra == ["A", "L", "E", "C", "R", "I", "M"]:
            print(palavra)
            break
elif escolha == "BAHIA":
    print("DICA: Time de futebol que já foi campeão Brasileiro")
    palavra = ["_", "_", "_", "_", "_"]
    erro = 0
    while palavra != ["B", "A", "H", "I", "A"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra == "B":
            palavra[0] = letra
            print(palavra)
        elif letra == "A":
            palavra[1] = letra
            palavra[4] = letra
            print(palavra)
        elif letra == "H":
            palavra[2] = letra
            print(palavra)
        elif letra == "I":
            palavra[3] = letra
            print(palavra)
        elif letra != "B" or letra != "A" or letra != "H" or letra != "I":
            print("ERROU A LETRA!!")
            erro = erro + 1
            if erro == 1:
                erro_01()
            elif erro == 2:
                erro_02()
            elif erro == 3:
                erro_03()
            elif erro == 4:
                erro_04()
            elif erro == 5:
                erro_05()
            elif erro == 6:
                erro_06()
                break
        elif palavra == ["B", "A", "H", "I", "A"]:
            print(palavra)
            break
elif escolha == "COQUEIRO":
    print("DICA: Árvore do litoral brasileiro de origem asiática")
    palavra = ["_", "_", "_", "_", "_", "_", "_", "_"]
    erro = 0
    while palavra != ["C", "O", "Q", "U", "E", "I", "R", "O"]:
        letra = str(input("Escolha uma letra: ")).upper().strip()
        if letra == "C":
            palavra[0] = letra
            print(palavra)
        elif letra == "O":
            palavra[1] = letra
            palavra[7] = letra
            print(palavra)
        elif letra == "Q":
            palavra[2] = letra
            print(palavra)
        elif letra == "U":
            palavra[3] = letra
            print(palavra)
        elif letra == "E":
            palavra[4] = letra
            print(palavra)
        elif letra == "I":
            palavra[5] = letra
            print(palavra)
        elif letra == "R":
            palavra[6] = letra
            print(palavra)
        elif letra != "C" or letra != "O" or letra != "Q" or letra != "U" or letra != "E" or letra != "I" or letra != "R":
            print("ERROU A LETRA!!")
            erro = erro + 1
            if erro == 1:
                erro_01()
            elif erro == 2:
                erro_02()
            elif erro == 3:
                erro_03()
            elif erro == 4:
                erro_04()
            elif erro == 5:
                erro_05()
            elif erro == 6:
                erro_06()
                break
        elif palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
            print(palavra)
            break
print("OBRIGADO E VOLTE SEMPRE!!")


