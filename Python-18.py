"""
Faça um programa para simular uma situação simples de depósito, retirada e consulta em um banco. Exiba o seguinte menu com as opções:

1 - Depósito
2 - Retirada
3 - Saldo
4 - Sair do algoritmo
Se a escolha do usuário for depósito ou retirada, o algoritmo deverá pedir o valor da operação e
atualizar automaticamente o valor existente na conta. O algoritmo deverá ser utilizado até que o usuário escolha a opção sair do algoritmo.
"""
valor_na_conta = [100000]
opcao = "ENTRAR"
while opcao != "SAIR":
    print("=" * 34)
    print("+===BEM VINDO AO BANCO CENTRAL===+")
    print("="*34)
    print("""
1 - Depósito
2 - Retirada
3 - Saldo
4 - Sair do algoritmo""")
    print("=" * 34)
    escolha = int(input("DIGITE UMA OPÇÃO: "))
    print("=" * 34)
    if escolha == 1:
        deposito = int(input("Quanto irá depositar? R$ "))
        depositado = valor_na_conta[0] + deposito
        valor_na_conta[0] = depositado
    elif escolha == 2:
            retira = int(input("Quanto irá retirar? R$ "))
            retirado = valor_na_conta[0] - retira
            valor_na_conta[0] = retirado
    elif escolha == 3:
            print(f"O SALDO ATUAL É DE R$ {valor_na_conta}")
    elif escolha == 4:
            opcao = "SAIR"

print("===OBRIGADO E VOLTE SEMPRE===")


