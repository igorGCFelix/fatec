def menu():
    a=False
    while not a:
        opcao = int(input("Escolha uma das opções: \n [1] Adicionar Nota \n [2] Consultar notas \n [3] Alterar notas \n [4] Excluir notas \n [5] Limpar terminal \n [0] Sair \n"))
        match opcao:
            case 1:
                adicionar_nota("João", 7.5)
                adicionar_nota("Maria Farah", 8.5)
                adicionar_nota("Henrique Lima", 7)
                adicionar_nota("Claudio José", 5.5)
            case 2:
                listar_notas(nomes, notas)
            case 3:
                alterar_nota(1, "João Silva", 6.5)
            case 4:
                excluir_nota(3)
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




