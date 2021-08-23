import random
import time


def venceu():
    for c in range(0, 3):
        print("   \033[1;33mW\033[m\033[1;33mW\033[m                   \033[1;33mW\033[m\033[1;33mW\033[m")
        time.sleep(0.3)
    print("  \033[30;42mPARABÉNS, VOCÊ VENCEU!!\033[m")


def fim():  # Função que finaliza o jogo.
    print()
    print()
    print("\033[1;33m            WW\033[m")
    time.sleep(0.2)
    print("\033[1;33m           ++++\033[m")
    time.sleep(0.2)
    print("\033[1;33m        +++++++++\033[m")
    time.sleep(0.2)
    print("\033[1;33m    ++++++++++++++++\033[m")
    time.sleep(0.2)
    print("\033[1;33m+++++++++++++++++++++++++\033[m")
    time.sleep(0.2)
    print("\033[1;31mOBRIGADO E VOLTE SEMPRE!!\033[m")
    time.sleep(0.2)
    print("\033[1;33m+++++++++++++++++++++++++\033[m")
    time.sleep(0.2)
    print("\033[1;33m    ++++++++++++++++\033[m")
    time.sleep(0.2)
    print("\033[1;33m        +++++++++\033[m")
    time.sleep(0.2)
    print("\033[1;33m           ++++\033[m")
    time.sleep(0.2)
    print("\033[1;33m            WW\033[m")


def forca_vazia():  # Função que inicializa o jogo
    print("==================")
    print("||                    ")
    print("||    JOGO DA FORCA   ")
    print("||   BY Fábio Barreto ")
    print("||                    ")
    print("||                    ")
    print("\033[1;32mxxxxxxxxxxxxxxxxxxx\033[m")


# Função quando erra a letra
def erro_01():
    print("==================")
    print("||     \033[7;30;41m(oo)\033[m      ")
    print("||                             ")
    print("||                             ")
    print("||                             ")
    print("||                             ")
    print("\033[1;32mxxxxxxxxxxxxxxxxxxx\033[m")


# Função quando erra a letra
def erro_02():
    print("==================")
    print("||      \033[7;30;41m(oo)\033[m      ")
    print("||       \033[7;30;41m||\033[m       ")
    print("||       \033[7;30;41m||\033[m       ")
    print("||                \033[m")
    print("||                \033[m")
    print("\033[1;32mxxxxxxxxxxxxxxxxxxx\033[m")


# Função do desenho quando erra a letra
def erro_03():
    print("==================")
    print("||      \033[7;30;41m(oo)\033[m      ")
    print("||       \033[7;30;41m||===\033[m    ")
    print("||       \033[7;30;41m||\033[m       ")
    print("||                ")
    print("||                ")
    print("\033[1;32mxxxxxxxxxxxxxxxxxxx\033[m")


# Função do desenho quando erra a letra
def erro_04():
    print("==================")
    print("||       \033[7;30;41m(oo)\033[m     ")
    print("||    \033[7;30;41m====||====\033[m  ")
    print("||        \033[7;30;41m||\033[m      ")
    print("||        \033[7;30;41m||\033[m      ")
    print("||                \033[m")
    print("||                \033[m")
    print("\033[1;32mxxxxxxxxxxxxxxxxxxx\033[m")


# Função do desenho quando erra a letra
def erro_05():
    print("==================")
    print("||       \033[7;30;41m(oo)\033[m      ")
    print("||    \033[7;30;41m====||====\033[m  ")
    print("||        \033[7;30;41m||\033[m      ")
    print("||       \033[7;30;41mMWWW\033[m     ")
    print("||      \033[7;30;41mMW\033[m        ")
    print("||     \033[7;30;41mMW\033[m         ")
    print("\033[1;32mxxxxxxxxxxxxxxxxxxx\033[m")


# Função do desenho quando erra a letra
def erro_06():
    print("==================")
    print("||      \033[7;30;41m(oo)\033[m      ")
    print("||    \033[7;30;41m===||===\033[m    ")
    print("||       \033[7;30;41m||\033[m       ")
    print("||      \033[7;30;41mMWWW\033[m      ")
    print("||     \033[7;30;41mMW\033[m  \033[7;30;41mMW\033[m     ")
    print("||    \033[7;30;41mMW\033[m    \033[7;30;41mMW\033[m    ")
    print("\033[1;32mxxxxxxxxxxxxxxxxxxx\033[m")
    print()
    print("\033[1;31;40mVOCÊ PERDEU!!\033[m")
    print(f"A palavra correta era \033[1;32;40m{escolha}!!\033[m")

# Função quando erra a letra
def erraLetraTexto():
    print()
    print("\033[1;31;40m===============\033[m")
    print("\033[1;31mERROU A LETRA!!\033[m")
    print("\033[1;31;40m===============\033[m")
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


# Lista dos nomes
lista_dos_nomes = ["TIBET", "NEUTRON", "URANO", "EINSTEIN", "ALECRIM", "BAHIA", "COQUEIRO"]
# Lista para detectar se já foi digitada alguma letra
lista_letras = []
# Escolhe um dos nomes na lista por sorteio
escolha = random.choice(lista_dos_nomes).upper().strip()


if escolha == "TIBET":
    forca_vazia()
    print("\033[7;31;40mDICA: País do centro asiático.\033[m")
    palavra = ["_", "_", "_", "_", "_"]
    print()
    for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
    print()
    erroMsg = 0
    while palavra != ["T", "I", "B", "E", "T"]:
        letra = str(input("\033[7;31;40mEscolha uma letra:\033[m ")).upper().strip()  # Independente se o suário digitar maiúsculo ou minúsculos, o upper() deixa tudo em maiúsculo como na lista principal e o strip para tirar o espaços caso alguém digite um.
        print()
        if letra in lista_letras:  # Avisa ao usuário que a letra já foi dita!
            print(f"\033[7;31;40mA letra {letra} já saiu, escolha novamente!!.\033[m")
            print()
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "T":
            palavra[0] = letra
            palavra[4] = letra
            lista_letras.append(letra)
            if palavra == ["T", "I", "B", "E", "T"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "I":
            palavra[1] = letra
            lista_letras.append(letra)
            if palavra == ["T", "I", "B", "E", "T"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "B":
            palavra[2] = letra
            lista_letras.append(letra)
            if palavra == ["T", "I", "B", "E", "T"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[3] = letra
            lista_letras.append(letra)
            if palavra == ["T", "I", "B", "E", "T"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "T" or letra != "I" or letra != "B" or letra != "E": # Caso as letras digitadas forem diferentes das contidas na palavra este bloco é ativado e aciona 2 funções
            erraLetraTexto()  # Função para alertar que o usuário errou a letra
            erroMsg = erroMsg + 1
            erro(erroMsg)  # Função que trabalha todos os erros e apresenta a forca e os desenhos
            if erroMsg == 6:
                break
elif escolha == "NEUTRON":
    forca_vazia()
    print("\033[7;31;40mDICA: Partícula subatômica.\033[m")
    palavra = ["_", "_", "_", "_", "_", "_", "_"]
    print()
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["N", "E", "U", "T", "R", "O", "N"]:
        letra = str(input("\033[7;31;40mEscolha uma letra:\033[m ")).upper().strip()
        print()
        if letra in lista_letras:
            print(f"\033[7;31;40mA letra {letra} já saiu, escolha novamente!!\033[m")
            print()
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "N":
            palavra[0] = letra
            palavra[6] = letra
            lista_letras.append(letra)
            if palavra == ["N", "E", "U", "T", "R", "O", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[1] = letra
            lista_letras.append(letra)
            if palavra == ["N", "E", "U", "T", "R", "O", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "U":
            palavra[2] = letra
            lista_letras.append(letra)
            if palavra == ["N", "E", "U", "T", "R", "O", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "T":
            palavra[3] = letra
            lista_letras.append(letra)
            if palavra == ["N", "E", "U", "T", "R", "O", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[4] = letra
            lista_letras.append(letra)
            if palavra == ["N", "E", "U", "T", "R", "O", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "O":
            palavra[5] = letra
            lista_letras.append(letra)
            if palavra == ["N", "E", "U", "T", "R", "O", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "N" or letra != "E" or letra != "B" or letra != "E":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "URANO":
    forca_vazia()
    print("\033[7;31;40mDICA: Planeta do Sistema Solar.\033[m")
    palavra = ["_", "_", "_", "_", "_"]
    print()
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["U", "R", "A", "N", "O"]:
        letra = str(input("\033[7;31;40mEscolha uma letra:\033[m ")).upper().strip()
        print()
        if letra in lista_letras:
            print(f"\033[7;31;40mA letra {letra} já saiu, escolha novamente!!\033[m")
            print()
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "U":
            palavra[0] = letra
            lista_letras.append(letra)
            if palavra == ["U", "R", "A", "N", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[1] = letra
            lista_letras.append(letra)
            if palavra == ["U", "R", "A", "N", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "A":
            palavra[2] = letra
            lista_letras.append(letra)
            if palavra == ["U", "R", "A", "N", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "N":
            palavra[3] = letra
            lista_letras.append(letra)
            if palavra == ["U", "R", "A", "N", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "O":
            palavra[4] = letra
            lista_letras.append(letra)
            if palavra == ["U", "R", "A", "N", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "U" or letra != "R" or letra != "A" or letra != "N" or letra != "O":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "EINSTEIN":
    forca_vazia()
    print("\033[7;31;40mDICA: Importante nome da física clássica.\033[m")
    palavra = ["_", "_", "_", "_", "_", "_", "_", "_"]
    print()
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["E", "I", "N", "S", "T", "E", "I", "N"]:
        letra = str(input("\033[7;31;40mEscolha uma letra:\033[m ")).upper().strip()
        print()
        if letra in lista_letras:
            print(f"\033[7;31;40mA letra {letra} já saiu, escolha novamente!!\033[m")
            print()
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "E":
            palavra[0] = letra
            palavra[5] = letra
            lista_letras.append(letra)
            if palavra == ["E", "I", "N", "S", "T", "E", "I", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[1] = letra
            palavra[6] = letra
            lista_letras.append(letra)
            if palavra == ["E", "I", "N", "S", "T", "E", "I", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "N":
            palavra[2] = letra
            palavra[7] = letra
            lista_letras.append(letra)
            if palavra == ["E", "I", "N", "S", "T", "E", "I", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "T":
            palavra[4] = letra
            lista_letras.append(letra)
            if palavra == ["E", "I", "N", "S", "T", "E", "I", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "S":
            palavra[3] = letra
            lista_letras.append(letra)
            if palavra == ["E", "I", "N", "S", "T", "E", "I", "N"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "E" or letra != "I" or letra != "N" or letra != "S" or letra != "T":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "ALECRIM":
    forca_vazia()
    print("\033[7;31;40mDICA: Erva aromática.\033[m")
    palavra = ["_", "_", "_", "_", "_", "_", "_"]
    print()
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["A", "L", "E", "C", "R", "I", "M"]:
        letra = str(input("\033[7;31;40mEscolha uma letra:\033[m ")).upper().strip()
        print()
        if letra in lista_letras:
            print(f"\033[7;31;40mA letra {letra} já saiu, escolha novamente!!\033[m")
            print()
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "A":
            palavra[0] = letra
            lista_letras.append(letra)
            if palavra == ["A", "L", "E", "C", "R", "I", "M"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "L":
            palavra[1] = letra
            lista_letras.append(letra)
            if palavra == ["A", "L", "E", "C", "R", "I", "M"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[2] = letra
            lista_letras.append(letra)
            if palavra == ["A", "L", "E", "C", "R", "I", "M"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "C":
            palavra[3] = letra
            lista_letras.append(letra)
            if palavra == ["A", "L", "E", "C", "R", "I", "M"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[4] = letra
            lista_letras.append(letra)
            if palavra == ["A", "L", "E", "C", "R", "I", "M"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[5] = letra
            lista_letras.append(letra)
            if palavra == ["A", "L", "E", "C", "R", "I", "M"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "M":
            palavra[6] = letra
            lista_letras.append(letra)
            if palavra == ["A", "L", "E", "C", "R", "I", "M"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "A" or letra != "L" or letra != "E" or letra != "C" or letra != "R" or letra != "I" or letra != "M":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "BAHIA":
    forca_vazia()
    print("\033[7;31;40mDICA: Time de futebol que já foi campeão Brasileiro.\033[m")
    palavra = ["_", "_", "_", "_", "_"]
    print()
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["B", "A", "H", "I", "A"]:
        letra = str(input("\033[7;31;40mEscolha uma letra:\033[m ")).upper().strip()
        print()
        if letra in lista_letras:
            print(f"\033[7;31;40mA letra {letra} já saiu, escolha novamente!!\033[m")
            print()
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "B":
            palavra[0] = letra
            lista_letras.append(letra)
            if palavra == ["B", "A", "H", "I", "A"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "A":
            palavra[1] = letra
            palavra[4] = letra
            lista_letras.append(letra)
            if palavra == ["B", "A", "H", "I", "A"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "H":
            palavra[2] = letra
            lista_letras.append(letra)
            if palavra == ["B", "A", "H", "I", "A"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[3] = letra
            lista_letras.append(letra)
            if palavra == ["B", "A", "H", "I", "A"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "B" or letra != "A" or letra != "H" or letra != "I":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break
elif escolha == "COQUEIRO":
    forca_vazia()
    print("\033[7;31;40mDICA: Árvore do litoral brasileiro de origem asiática.\033[m")
    palavra = ["_", "_", "_", "_", "_", "_", "_", "_"]
    print()
    for p in palavra: print(f"{p}", end=" ")
    print()
    erroMsg = 0
    while palavra != ["C", "O", "Q", "U", "E", "I", "R", "O"]:
        letra = str(input("\033[7;31;40mEscolha uma letra:\033[m ")).upper().strip()
        print()
        if letra in lista_letras:
            print(f"\033[7;31;40mA letra {letra} já saiu, escolha novamente!!\033[m")
            print()
            for p in palavra: print(f"{p}", end=" ")  # Uso o "for" para printar na tela apenas as letras, sem precisar dos colchetes em forma de lista
            print()
        elif letra == "C":
            palavra[0] = letra
            lista_letras.append(letra)
            if palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "O":
            palavra[1] = letra
            palavra[7] = letra
            lista_letras.append(letra)
            if palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "Q":
            palavra[2] = letra
            lista_letras.append(letra)
            if palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "U":
            palavra[3] = letra
            lista_letras.append(letra)
            if palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "E":
            palavra[4] = letra
            lista_letras.append(letra)
            if palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "I":
            palavra[5] = letra
            lista_letras.append(letra)
            if palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra == "R":
            palavra[6] = letra
            lista_letras.append(letra)
            if palavra == ["C", "O", "Q", "U", "E", "I", "R", "O"]:
                venceu()
                break
            for p in palavra: print(f"{p}", end=" ")
            print()
        elif letra != "C" or letra != "O" or letra != "Q" or letra != "U" or letra != "E" or letra != "I" or letra != "R":
            erraLetraTexto()
            erroMsg = erroMsg + 1
            erro(erroMsg)
            if erroMsg == 6:
                break

fim()

