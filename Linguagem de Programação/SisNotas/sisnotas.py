#Passar essa estrutura para um dicionário de dados
#Trabalhar com a manipulação de arquivos

import json
#importando a biblioteca OS para eu poder verificar se existe um arquivo
import os

def menu():
    a = False
    while not a:
        opcao = int(input("Escolha uma das opções: \n [1] Adicionar Nota \n [2] Consultar notas \n [3] Alterar notas \n [4] Excluir notas \n [5] Limpar terminal \n [0] Sair \n"))
        match opcao:
            case 1:
                #Adicionar Nota
                nome = receber_nome()
                nota = receber_media()
                adicionar_nota(alunos, nome, nota)
                print("\nAluno e média adicionados com sucesso!")

            case 2:
                #Consultar notas
                listar_notas(alunos)
                
                
            case 3:
                #Alterar notas
                chave = input("Digite o índice do aluno que você deseja alterar: \n")
                chave = validar_chave(chave)
                if chave is not None:
                    print(f"Nome do aluno: {alunos[chave][0]}, média do aluno: {alunos[chave][1]}")

                    continuar=deseja_continuar()
                
                    if continuar: 
                        nome = input("Digite o novo nome do aluno: \n")
                        nota = input("Digite a nova nota do aluno: \n ")
                    
                        continuar=deseja_continuar
                    
                        if continuar: alterar_nota(chave, nome, nota)
                        else: print("Operação cancelada.")
                    
                    else: print("Operação cancelada")
                         
                        
            case 4:
                #Excluir notas
                # fazer o fluxo alternativo
                chave = input("Digite o índice do aluno que deseja excluir: \n")
                chave = validar_chave(chave)
                if chave is not None:
                    print(f"Nome do aluno: {alunos[chave][0]}, média do aluno: {alunos[chave][1]}")
                    
                    continuar=deseja_continuar()
                    
                    if continuar:excluir_nota(chave)
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
                

# -------------------------------------------------------------------------------------------------

def iniciar_arquivo_json():
    nome_arquivo = "alunos.json"
    if os.path.exists(nome_arquivo):
            with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
                alunos = json.load(arquivo)
                return alunos
    else:
        alunos = {}
        return alunos

def adicionar_nota(alunos, nome, nota):
    chave=str(len(alunos)+1)
    alunos[chave] = {"nome": nome, "nota": nota}
    
    with open("alunos.json", "w", encoding="utf-8") as arquivoSisNotas:
        json.dump(alunos, arquivoSisNotas, ensure_ascii=False, indent=4)

def listar_notas(alunos):
    if alunos == {}:
        print("Não há alunos/notas para exibir")
    else:
        print("--- Lista ---")
        for nome, nota in alunos:
            print(nome, nota)

def excluir_nota(chave):
    alunos.pop(chave)

def alterar_nota(chave, nome, nota):
    alunos[chave] = [nome, nota]
    
# -------------------------------------------------------------------------------------------------


def validar_chave(chave):
    try: 
        chave = int(chave)
        if  chave >= len(alunos) or chave < 0:
            print("O índice inserido não existe na lista de alunos. Verifique os alunos ja cadastrados realizando a Consulta de Notas [2]")
            print("Operação cancelada.")
            return None
        else:
            return chave
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




# -------------------------------------------------------------------------------------------------

"""
Dicionário
alunos = {
    1:{},
    2:{}
}
"""

alunos = iniciar_arquivo_json()
menu()
