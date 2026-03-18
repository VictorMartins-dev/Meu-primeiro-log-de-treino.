
# Programa de Treino - Cadastro e Histórico
import os 

def exibir_menu():
    print("\n" + "="*20)
    print("PROGRAMA DE TREINO")
    print("="*20)
    print("1. Cadastrar Treino")
    print("2. Exibir Histórico de Treinos")
    print("3. Sair")
    return input("Escolha uma opção: ") 

while True:
    opcao = exibir_menu()
    
    if opcao == "1":
        nome = input("Digite seu nome: ")
        peso_atual = float(input("Digite seu peso atual: "))
        idade = int(input("Digite sua idade: "))
        aluno_academia = input("Voce é aluno da academia? (True/False) ")
        dias = input("Digite os dias da semana que voce irá treinar: ")
        total_dias_mes = int(input("Digite o total de dias do mês: "))
        semanas_no_mes = int(total_dias_mes / 7)
        horario_treino = input("Digite o horário do seu treino: ")
        dias_treino = input("Quantos dias voce irá treinar por semana? ")
        peso_futuro = float(input("Digite o peso que deseja alcançar: "))
        treinos_mensais = int(int(dias_treino) * (semanas_no_mes))
        
        with open("treino.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"Nome: {nome}\n")
            arquivo.write(f"Peso Atual: {peso_atual} kg\n")
            arquivo.write(f"Idade: {idade} anos\n")
            arquivo.write(f"Aluno da Academia: {aluno_academia}\n")
            arquivo.write(f"Dias de Treino: {dias}\n")
            arquivo.write(f"Total de Dias no Mês: {total_dias_mes}\n")
            arquivo.write(f"Semanas no Mês: {semanas_no_mes}\n")
            arquivo.write(f"Horário do Treino: {horario_treino}\n")
            arquivo.write(f"Dias de Treino por Semana: {dias_treino}\n")
            arquivo.write(f"Peso Futuro: {peso_futuro} kg\n")
            arquivo.write(f"Treinos Mensais: {treinos_mensais}\n")
            arquivo.write("\n")         
            
    elif opcao == "2":
        if os.path.exists("treino.txt"):
            with open("treino.txt", "r", encoding="utf-8") as arquivo:
                print("\nHISTÓRICO DE TREINOS:")
                print(arquivo.read())
        else:
            print("\nNenhum treino cadastrado ainda.")
            
    elif opcao == "3":
        print("\nSaindo do programa. Até mais!")
        break   
