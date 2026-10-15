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
                listar_notas(nomes, notas)
                
                
            case 3:
                #Alterar notas
                # fazer o fluxo alternativo
                
                indice = int(input("Digite o índice do aluno que você deseja alterar: \n"))
                if validar_indice(indice):
                    print(f"Nome do aluno: {nomes[indice]}, média do aluno: {notas[indice]}")

                    continuar=deseja_continuar()
                
                    if continuar: 
                        nome = input("Digite o novo nome do aluno")
                        nota = input("Digite a nova nota do aluno ")
                    
                        continuar=deseja_continuar
                    
                        if continuar: alterar_nota(indice, nome, nota)
                        else: print("Operação cancelada.")
                    
                    else: print("Operação cancelada")
                         
                        
            case 4:
                #Excluir notas
                indice = input("Digite o índice do aluno que deseja excluir")
                print(
                    f"Nome do aluno: {nomes[indice]}, média do aluno: {notas[indice]}")
                input("Deseja continuar? (S/N) \n")
                excluir_nota(indice)
                
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
    nomes.append(nome)
    notas.append(nota)

def listar_notas(nomes, notas):
    if nomes == []:
        print("Não há alunos/notas para exibir")
    else:
        print("--- Lista ---")
        for item in range(len(nomes)):
            print(
                f"Aluno: {nomes[item]}, Média: {notas[item]}, Índice: {item}")

def excluir_nota(indice):
    notas.pop(indice)
    nomes.pop(indice)

def alterar_nota(indice, nome, nota):
    nomes[indice] = nome
    notas[indice] = nota



def validar_indice(indice):
    try: 
        if  indice > len(nomes) or indice < 0:
            print("O índice inserido não existe na lista de alunos. Verifique os alunos ja cadastrados realizando a **Consulta de Notas [2]**")
            print("Operação cancelada.")
        else:
            return indice
    except ValueError:
        print("Certifique-se de digitar somente números inteiros para se referir ao índice.")

def receber_nome():
    a = False
    while not a:
        nome = input("Digite o nome do aluno: \n")
        #verificando se o usuário n digitou algum número no nome
        tem_numero = any(char.isdigit() for char in nome)
        
        if tem_numero:
            print("O nome digitado é inválido pela existência de um algarismo! \n")
        #vou usar o .strip() para que o jumento do usuário n passe só com o espaço
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

nomes = []
notas = []
menu()
