def jogada02(tabuleiro, jogada):
    if jogada == 2 and tabuleiro["A"][1] == "O":tabuleiro["B"][1] = "X"  # A2
    elif jogada == 2 and tabuleiro["A"][2] == "O":tabuleiro["C"][0] = "X"  # A3
    elif jogada == 2 and tabuleiro["B"][0] == "O":tabuleiro["B"][1] = "X"  # B1
    elif jogada == 2 and tabuleiro["B"][1] == "O":tabuleiro["A"][2] = "X"  # B2
    elif jogada == 2 and tabuleiro["B"][2] == "O":tabuleiro["C"][0] = "X"  # B3
    elif jogada == 2 and tabuleiro["C"][0] == "O":tabuleiro["A"][2] = "X"  # C1
    elif jogada == 2 and tabuleiro["C"][1] == "O":tabuleiro["A"][2] = "X"  # C2
    elif jogada == 2 and tabuleiro["C"][2] == "O":tabuleiro["B"][1] = "X"  # C3

    return tabuleiro


def jogada03(tabuleiro, jogada):
    if (jogada == 3 and tabuleiro["C"][2] == "O") and (tabuleiro["A"][1] == "O"): tabuleiro["B"][0] = "X"  # A2
    elif (jogada == 3 and tabuleiro["B"][0] == "O") and (tabuleiro["A"][2] == "O"): tabuleiro["B"][1] = "X"  # A3
    elif (jogada == 3 and tabuleiro["C"][2] == "O") and (tabuleiro["B"][0] == "O"): tabuleiro["A"][1] = "X"  # B1
    elif (jogada == 3 and tabuleiro["A"][1] == "O") and (tabuleiro["B"][1] == "O"): tabuleiro["C"][1] = "X"  # B2
    elif (jogada == 3 and tabuleiro["B"][0] == "O") and (tabuleiro["B"][2] == "O"): tabuleiro["B"][1] = "X"  # B3
    elif (jogada == 3 and tabuleiro["A"][1] == "O") and (tabuleiro["C"][0] == "O"): tabuleiro["C"][2] = "X"  # C1
    elif (jogada == 3 and tabuleiro["A"][1] == "O") and (tabuleiro["C"][1] == "O"): tabuleiro["B"][1] = "X"  # C2
    elif (jogada == 3 and tabuleiro["C"][0] == "O") and (tabuleiro["C"][2] == "O"):tabuleiro["C"][1] = "X"  # C3
    elif (jogada == 3 and tabuleiro["B"][2] == "O") and (tabuleiro["C"][2] == "O"):tabuleiro["A"][2] = "X"  # C3


    return tabuleiro


def jogada04(tabuleiro, jogada):
    if (jogada == 4 and tabuleiro["C"][0] == "O") and (tabuleiro["C"][2] == "O") and (tabuleiro["A"][1] == "O"):tabuleiro["B"][2] = "X"  # A2
    elif (jogada == 4 and tabuleiro["B"][2] == "O") and (tabuleiro["C"][2] == "O") and (tabuleiro["A"][1] == "O"):tabuleiro["C"][0] = "X"  # A2
    elif (jogada == 4 and tabuleiro["C"][2] == "O") and (tabuleiro["B"][0] == "O") and (tabuleiro["A"][2] == "O"):tabuleiro["C"][1] = "X"  # A3
    elif (jogada == 4 and tabuleiro["C"][0] == "O") and (tabuleiro["C"][2] == "O") and (tabuleiro["B"][0] == "O"):tabuleiro["A"][2] = "X"  # B1
    elif (jogada == 4 and tabuleiro["C"][1] == "O") and (tabuleiro["C"][2] == "O") and (tabuleiro["B"][0] == "O"):tabuleiro["A"][2] = "X"  # B1
    elif (jogada == 4 and tabuleiro["A"][2] == "O") and (tabuleiro["C"][2] == "O") and (tabuleiro["B"][0] == "O"):tabuleiro["C"][1] = "X"  # B1
    elif (jogada == 4 and tabuleiro["B"][0] == "O") and (tabuleiro["B"][1] == "O") and (tabuleiro["A"][1] == "O"):tabuleiro["B"][2] = "X"  # B2
    elif (jogada == 4 and tabuleiro["B"][2] == "O") and (tabuleiro["B"][1] == "O") and (tabuleiro["A"][1] == "O"):tabuleiro["B"][0] = "X"  # B2
    elif (jogada == 4 and tabuleiro["C"][2] == "O") and (tabuleiro["B"][2] == "O") and (tabuleiro["B"][0] == "O"):tabuleiro["A"][2] = "X"  # B3
    elif (jogada == 4 and tabuleiro["A"][2] == "O") and (tabuleiro["B"][2] == "O") and (tabuleiro["B"][0] == "O"):tabuleiro["C"][2] = "X"  # B3
    elif (jogada == 4 and tabuleiro["B"][2] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["C"][0] == "O"):tabuleiro["B"][1] = "X"  # C1
    elif (jogada == 4 and tabuleiro["B"][1] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["C"][0] == "O"):tabuleiro["B"][2] = "X"  # C1
    elif (jogada == 4 and tabuleiro["C"][0] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["C"][1] == "O"):tabuleiro["C"][2] = "X"  # C2
    elif (jogada == 4 and tabuleiro["C"][2] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["C"][1] == "O"):tabuleiro["C"][0] = "X"  # C2
    elif (jogada == 4 and tabuleiro["A"][1] == "O") and (tabuleiro["C"][0] == "O") and (tabuleiro["C"][2] == "O"):tabuleiro["C"][0] = "X"  # C3
    elif (jogada == 4 and tabuleiro["A"][1] == "O") and (tabuleiro["B"][2] == "X") and (tabuleiro["C"][2] == "O"):tabuleiro["C"][0] = "X"  # C3
    elif (jogada == 4 and tabuleiro["C"][0] == "O") and (tabuleiro["B"][2] == "O") and (tabuleiro["C"][2] == "O"):tabuleiro["A"][1] = "X"  # C3

    return tabuleiro


def jogada05(tabuleiro, jogada):
    if (jogada == 5 and tabuleiro["A"][1] == "O") and (tabuleiro["C"][2] == "O") and (tabuleiro["B"][0] == "O") and (tabuleiro["A"][2] == "O"):tabuleiro["B"][2] = "X"  # A3
    elif (jogada == 5 and tabuleiro["C"][2] == "O") and (tabuleiro["B"][1] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["B"][0] == "O"):tabuleiro["C"][0] = "X"  # B2
    elif (jogada == 5 and tabuleiro["C"][0] == "O") and (tabuleiro["B"][1] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["A"][2] == "X"):tabuleiro["C"][2] = "X"  # B2
    elif (jogada == 5 and tabuleiro["B"][2] == "O") and (tabuleiro["B"][2] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["C"][0] == "O"):tabuleiro["A"][2] = "X"  # C1
    elif (jogada == 5 and tabuleiro["B"][0] == "O") and (tabuleiro["A"][1] == "O") and (tabuleiro["C"][2] == "O") and (tabuleiro["C"][0] == "O"):tabuleiro["A"][2] = "X"  # C3
    elif (jogada == 5 and tabuleiro["C"][1] == "O") and (tabuleiro["A"][1] == "X") and (tabuleiro["C"][2] == "O") and (tabuleiro["A"][2] == "O"):tabuleiro["C"][0] = "X"  # C3

    return tabuleiro
