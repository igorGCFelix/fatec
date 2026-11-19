#Passar essa estrutura para um dicionário de dados
#Trabalhar com a manipulação de arquivos

import json
#importando a biblioteca OS para eu poder verificar se existe um arquivo
import os

#definindo o caminho absoluto com base no local do arquivo .py
pasta = os.path.dirname(os.path.abspath(__file__))
caminho_json = os.path.join(pasta, "alunos.json")

# -------------------------------------------------------------------------------------------------
#Função menu
            
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
                chave = input("Digite a chave do aluno que você deseja alterar: \n")
                chave = validar_chave(chave)
                if chave is not None:
                    print(f"Nome do aluno: {alunos[chave]["nome"]}, média do aluno: {alunos[chave]["nota"]}")

                    continuar=deseja_continuar()
                
                    if continuar: 
                        nome = input("Digite o novo nome do aluno: \n")
                        nota = input("Digite a nova nota do aluno: \n")
                    
                        continuar=deseja_continuar
                    
                        if continuar: alterar_nota(chave, nome, nota)
                        else: print("Operação cancelada.")
                    
                    else: print("Operação cancelada")
                         
                        
            case 4:
                #Excluir notas
                chave = input("Digite o índice do aluno que deseja excluir: \n")
                chave = validar_chave(chave)
                if chave is not None:
                    print(f"Nome do aluno: {alunos[chave]["nome"]}, média do aluno: {alunos[chave]["nota"]}")
                    
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
#Manipulação JSON

def iniciar_arquivo_json():
    if os.path.exists(caminho_json):
        with open(caminho_json, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    else:
        return {}
    
def write_arquivo_json(alunos):
    with open(caminho_json, "w", encoding="utf-8") as arquivoSisNotas:
            json.dump(alunos, arquivoSisNotas, ensure_ascii=False, indent=4)

# -------------------------------------------------------------------------------------------------
#Funçoes de adicionar/listar/excluir/alterar

def adicionar_nota(alunos, nome, nota):
    chave=str(len(alunos)+1)
    alunos[chave] = {"nome": nome, "nota": nota}
    
    write_arquivo_json(alunos)

def listar_notas(alunos):
    if not alunos:
        print("Não há alunos/notas para exibir")
    else:
        print("--- Lista ---")
        
        for chave, dados in alunos.items(): #vai percorrer os items do dicionário
            print(f"Chave: {chave}; Nome: {dados["nome"]}; Média: {dados["nota"]}")
        
def excluir_nota(chave):
    del alunos[chave]
    write_arquivo_json(alunos)
    
def alterar_nota(chave, nome, nota):
    alunos[chave] = {"nome": nome, "nota": nota}
    write_arquivo_json(alunos)
    
# -------------------------------------------------------------------------------------------------
#Funções que se repetem muito

def validar_chave(chave):
    if chave not in alunos:
        print("O índice inserido não existe. Consulte as notas [2] para ver os alunos cadastrados.")
        print("Operação cancelada.")
        return None
    return chave

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

alunos = iniciar_arquivo_json()
menu()
