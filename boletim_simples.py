
import os

def exibir_menu():
    print("\n" + "="*4)
    print("BOLETIM ESCOLAR")
    print("="*4)
    print("1. Cadastrar Notas")
    print("2. Exibir Boletim")
    print("3. Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = exibir_menu()
    
    if opcao == "1":
        nome = input("Digite seu nome: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        nota4 = float(input("Digite a quarta nota: "))
        media = float(nota1 + nota2 + nota3 + nota4) / 4
        status = "Aprovado" if media >= 6 else "Recuperação" if media >= 5 else "Reprovado"
        
        with open("boletim.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"Nota 1: {nota1}\n")
            arquivo.write(f"Nota 2: {nota2}\n")
            arquivo.write(f"Nota 3: {nota3}\n")
            arquivo.write(f"Nota 4: {nota4}\n")
            arquivo.write(f"Média: {media:.1f}\n")
            arquivo.write(f"Status: {status}\n")
            arquivo.write("\n")         
            
    elif opcao == "2":
        if os.path.exists("boletim.txt"):
            with open("boletim.txt", "r", encoding="utf-8") as arquivo:
                print("\nBOLETIM ESCOLAR:")
                print(arquivo.read())
        else:
            print("\nNenhum boletim cadastrado ainda.")
            
    elif opcao == "3":
        print("\nSaindo do programa. Até mais!")
        break