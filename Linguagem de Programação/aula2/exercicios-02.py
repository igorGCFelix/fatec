# 1
print("--- EXERCÍCIO 1 ---")
while True:
    numero = int(input("Digite um número inteiro e positivo: \n"))
    if numero > 0:
        break

if numero % 2 == 0:
    print("O número é par")
else:
    print("O número é ímpar")

# 2
print("--- EXERCÍCIO 2 ---")
while True:
    peso = float(input("Digite o peso do indivíduo em decimal: \n"))
    if peso > 0:
        break
while True:
    altura = float(input("Digite a altura do indivíduo em decimal: \n"))
    if altura > 0:
        break

imc = peso/altura**2
print("O IMC do indivíduo é: ", imc)
if imc < 18.5:
    print("O indivíduo está abaixo do peso")
elif imc < 24.9:
    print("O indivíduo está com o peso normal")
elif imc < 29.9:
    print("O indivíduo está sobrepeso")
else:
    print("O indivíduo está com obesidade")

# #3
print("--- EXERCÍCIO 3 ---")
# agora a nota máxima é 10

a1 = float(input("Digite a primeira nota: \n"))
a2 = float(input("Digite a segunda nota: \n"))
if (a1 < 0 or a1 > 10 or a2 < 0 or a2 > 10):
    print("Nota de A1 e/ou A2 inválida")
    #eu faria um loop, mas a atividade pediu assim
else:
    media = (a1+a2)/2
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
