
import os 

def exibir_menu():
    print("\n" + "="*20)
    print("Sistema de Cadastro de Clientes")
    print("="*20)
    print("1. Cadastrar Cliente")
    print("2. Excluir Histórico de Clientes")
    print("3. Exibir Histórico de Clientes")
    print("4. Sair do Programa")
    return input("Escolha uma opção: ")

import os
    
arquivo_nome = "clientes.txt"
if os.path.exists(arquivo_nome):
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        print("\nHISTÓRICO DE CLIENTES:")
        print(arquivo.read())
while True:

    opcao = exibir_menu()
    
    if opcao == "1":
        nome = input("Digite o nome do cliente: ")
        sobrenome = input("Digite o sobrenome do cliente: ")
        try:
            idade = int(input("Digite a idade do cliente: "))
        except ValueError:
            print("Idade inválida. Por favor, digite um número.")
            continue
        CPF = input("Digite o CPF do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        horário = input("Digite o horário de atendimento preferencial do cliente (manhã/tarde/noite): ")    
        print("Cadastro realizado com sucesso!")
        print("Dados do cliente:")                                                      
        with open("clientes.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"Sobrenome: {sobrenome}\n")
            arquivo.write(f"Idade: {idade} anos\n")
            arquivo.write(f"CPF: {CPF}\n")
            arquivo.write(f"Endereço: {endereco}\n")
            arquivo.write(f"Horário de Atendimento Preferencial: {horário}\n")
            arquivo.write("\n")
    elif opcao == "2":
        if os.system("cls" if os.name == "nt" else "clear") == 0:
            print("Excluir histórico de clientes")
            if os.path.exists("clientes.txt"):
                os.remove("clientes.txt")
                print("Histórico de clientes excluído com sucesso!")
            else:
                print("Nenhum histórico de clientes encontrado.")
    elif opcao == "3":
        if os.path.exists("clientes.txt"):
            with open("clientes.txt", "r", encoding="utf-8") as arquivo:
                print("\nHISTÓRICO DE CLIENTES:")
                print(arquivo.read())
        else:   
            print("Não há historico de clientes para exibir.")
    elif opcao == "4":      
        if os.path.exists("clientes.txt"):
            with open("clientes.txt", "r", encoding             ="utf-8") as arquivo:           
                print("\nHISTÓRICO DE CLIENTES:")
                print(arquivo.read())   
        else:
            print("\nSaindo do programa. Até mais!")

        break