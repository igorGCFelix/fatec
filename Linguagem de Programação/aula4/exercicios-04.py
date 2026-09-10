#1
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
alunos = []
medias = []

i = 0
while i < 1: 
    aluno = input("Digite o nome do aluno: \n")
    alunos.append(aluno)
    media = input("Digite a média do aluno: \n")
    medias.append(media)

    a=0
    while a < 1:
        continuar=input("Deseja continuar adicionando notas? (S/N): \n")
        if continuar.upper() == "N":
            alunoX=input("Digite o nome do aluno que você quer ver a média: \n")
            idx = alunos.index(alunoX)
            print(f"Aluno: {alunos[idx]}, Média: {medias[idx]}")
            a = 1
            i = 1
        elif continuar.upper() == "S":
            a=1
        else:
            print("Escolha entre a opção (S/N)!")
