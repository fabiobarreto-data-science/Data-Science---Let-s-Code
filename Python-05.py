# Desafio 3 - Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de um questionário de sintomas, tendo as perguntas a o diagnóstico deste hospital:

A = str(input("Sente dor de cabeça? (SIM/NÃO)")).upper().strip()
B = str(input("Você tem febre? (SIM/NÃO)")).upper().strip()
C = str(input("Você tem tosse? (SIM/NÃO)")).upper().strip()
D = str(input("Está com congestão nasal? (SIM/NÃO)")).upper().strip()
E = str(input("Tem manchas pelo corpo? (SIM/NÃO)")).upper().strip()
if A == "SIM" and B == "SIM" and C == "NÃO" and D == "NÃO" and E == "SIM":
    print(f"O paciente está com dengue.")
else:
    if A == "SIM" and B == "SIM" and C == "SIM" and D == "SIM" and E == "NÃO":
        print(f"O paciente está com gripe.")
    else:
        if A == "NÃO" and B == "SIM" and C == "SIM" and D == "SIM" and E == "NÃO":
            print(f"O paciente está com gripe.")
        else:
            if (A == "SIM" and B == "NÃO" and C == "NÃO" and D == "NÃO" and E == "NÃO") or (A == "NÃO" and B == "NÃO" and C == "NÃO" and D == "NÃO" and E == "NÃO"):
                print(f"O paciente não está doente.")