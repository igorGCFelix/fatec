#1
# print ("--- EXERCÍCIO 1 ---")
# while True:
#     numero = int(input("Digite um número inteiro e positivo: \n"))
#     if numero > 0:
#         break

# if numero % 2 == 0:
#     print("O número é par")
# else:
#     print("O número é ímpar")

#2
# print ("--- EXERCÍCIO 2 ---")
# while True:
#     peso = float(input("Digite o peso do indivíduo: \n"))
#     if peso > 0:
#         break
# while True:
#     altura = float(input("Digite a altura do indivíduo: \n"))
#     if altura >0:
#         break

# imc = peso/altura**2
# print("O IMC do indivíduo é: ",imc)
# if imc < 18.5:
#     print("O indivíduo está abaixo do peso")
# elif imc <24.9:
#     print("O indivíduo peso normal")
# elif imc<29.9:
#     print("O indivíduo sobrepeso")
# else:
#     print("O indivíduo obesidade")

# #3
print ("--- EXERCÍCIO 3 ---")
# agora a nota máxima é 10
while True:
    a1 = float(input("Digite a primeira nota: \n"))
    if a1 >=0:
        break

while True:
    a2 = float(input("Digite a segunda nota: \n"))
    if a2 >=0:
        break

media = (a1+a2)/2
print ("A média do aluno é ",media, "\n")

if media >= 6: print("Aluno aprovado!")
else: 
    print("Aluno deverá realizar a prova substitutiva!")
    if a1<a2:
        notaNecessaria=12-a2
        print("A nota necessária será: ",notaNecessaria)
        
    else: 
        notaNecessaria=12-a1
        print("A nota necessária será: ",notaNecessaria)


        


