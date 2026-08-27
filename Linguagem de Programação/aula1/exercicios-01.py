# 1
print ("--- EXERCÍCIO 1 ---")
nome = input("Digite o seu nome:\n")
print ("Olá,",nome, "!\n")

# 2
print ("--- EXERCÍCIO 2 ---")
# não está falando se a nota é até 10
a1 = float(input("Digite a primeira nota: \n"))
a2 = float(input("Digite a segunda nota: \n"))
media = (a1+a2)/2
print ("A média do aluno é ",media, "\n")

#3
print ("--- EXERCÍCIO 3 ---")
#não falou se existe ou n desconto de 100%
preco = float(input("Digite o preco do produto: \n"))
desconto = float(input("Digite o percentual de desconto do produto: \n"))
valorFinal = preco - (desconto*preco/100)
print (f"O valor final do produto é: R${valorFinal}")