# #1
print("---Exercício 1---")
print("---for---")
for i in range (10, 0, -1):
    if i % 2 == 0:
        print(i)
print("---while---")
i = 10
while i >= 1:
    if i % 2 == 0:
        print(i)
    i = i - 1 

# #2
print("---Exercício 2---")
print("---for---")
for i in range(1, 6):
    print(i**2)
print("---while---")
i = 1
while i<=5:
    print(i**2)
    i=i+1

#3
print("---Exercício 3---")
numero = int(input("Digite um número inteiro: \n"))
print("---for---")
for i in range (0, 10):
    print(numero*i)

print("---while---")
i = 0
while i < 10:
    print(numero*i)
    i = i + 1

#4
print("---Exercício 4---")
numero = int(input("Digite um número inteiro e positivo: \n"))
if numero < 0:
    print("Erro! Digite um número positivo!")
else:
    print("---for---")
    for i in range (0, 10):
        print(numero*i)

    print("---while---")
    i = 0
    while i < 10:
        print(numero*i)
        i = i + 1