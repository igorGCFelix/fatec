#CENÁRIO DE SUCESSO DO FLUXO PRINCIPAL DE SUCESSO
def menu():
    a=False
    while not a:
        opcao = int(input("Escolha uma das opções: \n [1] Adicionar Nota \n [2] Consultar notas \n [3] Alterar notas \n [4] Excluir notas \n [5] Limpar terminal \n [0] Sair \n"))
        match opcao:
            case 1:
                nome = input("Digite o nome do aluno: \n")
                nota = float(input("Digite a nota do aluno: \n"))
                adicionar_nota(nome, nota)
                
            case 2:
                listar_notas(nomes, notas)
            case 3:
                indice = input("Digite o índice do aluno que você deseja alterar: \n")
                print(f"Nome do aluno: {nomes[indice]}, média do aluno: {notas[indice]}")
                input("Deseja continuar? (S/N) \n")

                nome = input("Digite o novo nome do aluno")
                nota = input("Digite a nova nota do aluno ")
                input("Deseja continuar? (S/N) \n")
                    
                alterar_nota(indice, nome, nota)
                      
            case 4:
                indice = input("Digite o índice do aluno que deseja excluir")
                print(f"Nome do aluno: {nomes[indice]}, média do aluno: {notas[indice]}")
                input("Deseja continuar? (S/N) \n")
                excluir_nota(indice)
            case 0:
                a = True
            case 5:
                print("\033[H\033[J", end="")
            case _:
                print("Valor inválido")


def adicionar_nota(nome, nota): 
    nomes.append(nome)
    notas.append(nota)

def listar_notas(nomes, notas): 
    print("--- Lista ---")
    for item in range(len(nomes)):
        print(f"Aluno: {nomes[item]}, Média: {notas[item]}, Índice: {item}")

def excluir_nota(indice):
    notas.pop(indice)
    nomes.pop(indice)

def alterar_nota(indice, nome, nota):
    nomes[indice] = nome
    notas[indice] = nota




# -----

nomes = []
notas = []
menu()




