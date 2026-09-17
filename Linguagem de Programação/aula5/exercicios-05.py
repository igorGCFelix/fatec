#1
def calcular_media(a1, a2):
    media = (a1+a2)/2
    return media

print("--- Exercício 1 ---")
atividade1 = float(input("Digite a nota da primeira atividade: \n"))
atividade2 = float(input("Digite a nota da segunda atividade: \n"))
media = calcular_media(atividade1,atividade2)
print(media)

#2
def validar_nota(nota):
    if nota<0 or nota>10:
        validarNota=False
        return validarNota
    else:
        validarNota=True
        return validarNota

print("--- Exercício 2 ---")
atividade1 = float(input("Digite a nota da primeira atividade: \n"))
validarNota1 = validar_nota(atividade1)
print("Nota: ", validarNota1)

atividade2 = float(input("Digite a nota da segunda atividade: \n"))
validarNota2 = validar_nota(atividade2)
print("Nota: ", validarNota2)

#3
def validar_nota(nota):
    if nota<0 or nota>10:
        validarNota=False
        return validarNota
    else:
        validarNota=True
        return validarNota
    
# jeito elegante
# def validar_nota(nota):
#     return 0 <= nota <= 10

def calcular_media(a1, a2):
    media = (a1+a2)/2
    return media

print("--- Exercício 3 ---")
a1 = float(input("Digite a primeira nota: \n"))
a2 = float(input("Digite a segunda nota: \n"))
validarA1 = validar_nota(a1)
validarA2 = validar_nota(a2)


if (not validarA1 or not validarA2):
    print("Nota de A1 e/ou A2 inválida")
    #o exercício pede desse jeito, A1 ou A2 inválida -> irei manter assim
else:
    media = calcular_media(a1, a2)
    print("A média do aluno é ", media, "\n")

    if media >= 6:
        print("Aluno aprovado!")
    else:
        print("Aluno deverá realizar a prova substitutiva!")
        # A média mínima para passar é 6, logo a soma mínima da média tem que ser de 12
        # 12/2 = 6 -> min para passar

        if a1 < a2:
            notaNecessaria = 12-a2
            print("A nota necessária para a prova substitutiva será: ", notaNecessaria)

        else:
            notaNecessaria = 12-a1
            print("A nota necessária para a prova substitutiva será: ", notaNecessaria)
