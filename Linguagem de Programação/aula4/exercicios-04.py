#FALTA EU VERIFICAR OS INDICES PEDIDOS PELO USUÁRIO
#melhor eu fazer função? -> professor falou nd entt nem meto o bedelho

#1
print("---Exercício 1 ---")
# lista de alunos e médias
# alunos = []
# medias = []

# i = 0
# while i < 1: 
#     aluno = input("Digite o nome do aluno: \n")
#     alunos.append(aluno)
#     media = input("Digite a média do aluno: \n")
#     medias.append(media)

#     a=0
#     while a < 1:
#         continuar=input("Deseja continuar adicionando notas? (S/N): \n")
#         if continuar.upper() == "N":
#             for item in range(len(alunos)):
#                 print(f"Aluno: {alunos[item]}, Média: {medias[item]}")
#             a = 1
#             i = 1
#         elif continuar.upper() == "S":
#             a=1
#         else:
#             print("Escolha entre a opção (S/N)!")

#2
print("---Exercício 2 ---")
# alunos = []
# medias = []

# i = 0
# while i < 1: 
#     aluno = input("Digite o nome do aluno: \n")
#     alunos.append(aluno)
#     media = input("Digite a média do aluno: \n")
#     medias.append(media)

#     a=0
#     while a < 1:
#         continuar=input("Deseja continuar adicionando notas? (S/N): \n")
#         if continuar.upper() == "N":
#             alunoX=input("Digite o nome do aluno que você quer ver a média: \n")
#             if alunoX not in alunos:
#                 print("Não há um aluno com esse nome. Tabela de alunos existentes e suas médias:")
#                 for item in range(len(alunos)):
#                     print(f"Aluno: {alunos[item]}, Média: {medias[item]}")
#                 a = 1
#                 i = 1

#             else:        
#                 idx = alunos.index(alunoX)
#                 print(f"Aluno: {alunos[idx]}, Média: {medias[idx]}")
#                 a = 1
#                 i = 1
#         elif continuar.upper() == "S":
#             a=1
#         else:
#             print("Escolha entre a opção (S/N)!")

#3
def verificarIndice(tamanho):
    i = 0
    while i < 1:
        try:
            indice=int(input("Digite o número do índice que deseja alterar: ")) 
            if indice < 0 or indice > tamanho:
                print("Valor inválido, digite novamente!")
            else: 
                print(f"Os dados do índice {indice}:\n Aluno: {nomes[indice]}, Média: {medias[indice]}")
                i=1
                return indice
        except ValueError:
            print("Digite um número inteiro")
        

print("---Exercício 3 ---")
nomes = [ "Ana", "Claudia", "Diego", "Diogo", "Elizia", "Fabricio", "Gabriella", "Marcelo", "Marcelly", "Tássia" ]
medias = [ 8.5, 6.0, 4.5, 6.5, 9.5, 5.5, 8.0, 4.0, 9.0, 2.5]

for item in range(len(nomes)):
    print(f"Aluno: {nomes[item]}, Média: {medias[item]}, Índice: {item}")

opcao=input("Escolha entre uma das opções: [A]lterar, [E]xcluir ou [S]air \n")
# 3A
if opcao.upper() == "A":
    #vai receber e verificar o indice
    indice = verificarIndice(len(nomes))

    #recebendo os novos valores
    nomeNovo=input("Digite o nome do aluno:")
    mediaNova=float(input("Digite a média do aluno: "))

    #confirmação das alterações
    b=0
    while b<1: 
        resposta = input("Deseja confirmar essas alterações (S/N)?")
        if resposta.upper() == "S":
            medias[indice] = mediaNova
            nomes[indice] = nomeNovo
            print("Alterações feitas com sucesso!")
            print(f"Alterações: Aluno {nomes[indice]}, Média {medias[indice]}")
            b=1
        elif resposta.upper() == "N":
            print("Alterações canceladas!")
            b=1
        else:
            print("Valor inválido, responda novamente.")

elif opcao.upper() == "E":
    indice=verificarIndice(len(nomes))

    #confirmação da exclusão
    b=0
    while b<1: 
        resposta = input("Deseja confirmar essa exclusão (S/N)?")
        if resposta.upper() == "S":
            nomes.pop(indice)
            medias.pop(indice)
            print("Exclusão feita com sucesso!")
            b=1
        elif resposta.upper() == "N":
            print("Exclusão cancelada!")
            b=1
        else:
            print("Valor inválido, responda novamente.")

