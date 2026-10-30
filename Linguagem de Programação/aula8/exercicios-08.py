# CENÁRIO DE SUCESSO DO FLUXO PRINCIPAL DE SUCESSO
def menu():
    a = False
    while not a:
        opcao = int(input("Escolha uma das opções: \n [1] Adicionar Nota \n [2] Consultar notas \n [3] Alterar notas \n [4] Excluir notas \n [5] Limpar terminal \n [0] Sair \n"))
        match opcao:
            case 1:
                #Adicionar Nota
                nome = receber_nome()
                nota = receber_media()
                adicionar_nota(nome, nota)
                print("\nAluno e média adicionados com sucesso!")

            case 2:
                #Consultar notas
                listar_notas(alunos)
                
                
            case 3:
                #Alterar notas
                indice = input("Digite o índice do aluno que você deseja alterar: \n")
                indice = validar_indice(indice)
                if indice is not None:
                    print(f"Nome do aluno: {alunos[indice][0]}, média do aluno: {alunos[indice][1]}")

                    continuar=deseja_continuar()
                
                    if continuar: 
                        nome = input("Digite o novo nome do aluno: \n")
                        nota = input("Digite a nova nota do aluno: \n ")
                    
                        continuar=deseja_continuar
                    
                        if continuar: alterar_nota(indice, nome, nota)
                        else: print("Operação cancelada.")
                    
                    else: print("Operação cancelada")
                         
                        
            case 4:
                #Excluir notas
                # fazer o fluxo alternativo
                indice = input("Digite o índice do aluno que deseja excluir: \n")
                indice = validar_indice(indice)
                if indice is not None:
                    print(f"Nome do aluno: {alunos[indice][0]}, média do aluno: {alunos[indice][1]}")
                    
                    continuar=deseja_continuar()
                    
                    if continuar:excluir_nota(indice)
                    else: print("Operação cancelada.")
                
            case 0:
                #Sair
                a = True
                
            case 5:
                #Limpar
                print("\033[H\033[J", end="")
                
            case _:
                #Jumento
                print("Valor inválido")


def adicionar_nota(nome, nota):
    alunos.append([nome, nota])

def listar_notas(alunos):
    if alunos == []:
        print("Não há alunos/notas para exibir")
    else:
        print("--- Lista ---")
        for nome, nota in alunos:
            print(nome, nota)

def excluir_nota(indice):
    alunos.pop(indice)

def alterar_nota(indice, nome, nota):
    alunos[indice] = [nome, nota]
    



def validar_indice(indice):
    try: 
        indice = int(indice)
        if  indice >= len(alunos) or indice < 0:
            print("O índice inserido não existe na lista de alunos. Verifique os alunos ja cadastrados realizando a Consulta de Notas [2]")
            print("Operação cancelada.")
            return None
        else:
            return indice
    except ValueError:
        print("Certifique-se de digitar somente números inteiros para se referir ao índice.")
        return None

def receber_nome():
    a = False
    while not a:
        nome = input("Digite o nome do aluno: \n")
        tem_numero = any(char.isdigit() for char in nome)
        
        if tem_numero:
            print("O nome digitado é inválido pela existência de um algarismo! \n")
        elif not nome.strip():
            print("Você deve preencher esse campo para prosseguir! \n")
        else:
            a = True
            
    return nome

def receber_media():
    
    a = False
    while not a:
        try:
            nota = float(input("Digite a nota do aluno: \n"))
            
            if nota < 0 or nota > 10:
                print("A nota inserida está fora do intervalo permitido (0 até 10)! \n")
            else:
                a = True
                
        except ValueError:
            print("Certifique-se de digitar somente números! \n")
            
    return nota

def deseja_continuar():
    a = False
    while not a:
        desejaContinuar = input("Deseja continuar? (S/N) \n")
        if desejaContinuar.upper() == "S":
            continuar=True
            a=True
        elif desejaContinuar.upper() == "N":
            continuar=False
            a = True
        else:
            print("Escolha uma opção válida: S/N")
    return continuar




# -------

#substituindo as LISTAS PARALELAS por uma MATRIZ
# nomes = []
# notas = []
# alunos = [
#     [nome1, nota1],
#     [nome2, nota2],
# ]

alunos = []
menu()
