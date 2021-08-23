"""
Enunciado
Super desafio! Faça um sistema de cadastro de clientes. Modele cada cliente como uma lista de três elementos: nome, CPF e e-mail.

a. Faça uma função que peça o nome, o CPF e o e-mail da pessoa e retorne uma lista contendo esses elementos nessa ordem.

b. Os clientes cadastrados devem ser armazenados em uma lista (uma lista de listas, já que cada cliente será uma lista tal como produzido no item a).

c. Faça uma função que recebe a lista do item b) e um CPF e, se esse cliente estiver na lista de cadastro, sua função deve devolver a lista de dados desse cliente; caso contrário,
 sua função deve imprimir “não encontrado”.

d. Enquanto não for digitado 0, o seu programa deve continuar rodando. Se digitado 1, seu programa deve cadastrar um novo cliente;
se digitado 2, seu programa deve pedir um CPF e procurá-lo na lista de clientes (item c); se digitado 3, seu programa deve imprimir todos os clientes cadastrados.
"""
lista_clientes = []
lista_cadastra_clientes = []


def cadastraClientes(lista_clientes):
    contador = 4
    while contador != 0:
        print("""
            0 - SAIR DO SISTEMA
            1 - CADASTRAR NOVO CLIENTE
            2 - DIGITE UM CPF
            3 - IMPRIMIR TODOS OS CLIENTES
            """)
        contador = int(input("Escolha uma opção: "))
        if contador == 0:
            break
        else:
            if contador == 1:
                nome = str(input("NOME: "))
                lista_clientes.append(nome)
                cpf = int(input("CPF: "))
                lista_clientes.append(cpf)
                email = str(input("E-MAIL: "))
                lista_clientes.append(email)
                print(lista_clientes)
            else:
                if contador == 2:
                    cpf = int(input("DIGITE O CPF PROCURADO: "))
                    cont = 0
                    while cont <= len(lista_clientes):
                        cliente = lista_clientes[cont]
                        cont = cont + 1
                        if cliente == cpf:
                            print(lista_clientes)
                else:
                    if contador == 3:
                        for c in lista_clientes:
                            print(lista_clientes[c])


cadastraClientes(lista_clientes)







