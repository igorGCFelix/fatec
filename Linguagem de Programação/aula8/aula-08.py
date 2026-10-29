#estrutura de daos serve para guardar coisas
#dicionario de dados é uma estrutura da dados que trabalha com CHAVE e VALOR

#estrutura de dados homogenea, trabalhando com listas paralelas unidimensionais
alunos = ["José", "João"]
notas = [7.5 , 8.5]

#estrutura de dados heterogenea -> matriz (listas bidimensionais -- X e Y)
matriz_notas = [
    ["José", 7.5],
    ["João", 8.5]
]
print("Lista completa")
print(matriz_notas)

# APPEND
print("Adicionando o igor na lista")
matriz_notas.append(["Igor", 10])
print(matriz_notas)

# POP
print("Deletando o último valor na lista")
matriz_notas.pop()
print(matriz_notas)

# POP COM INDICE
print("Deletando o valor (0, 1) -> nota do josé")
matriz_notas[0].pop(1)
print(matriz_notas)

# REMOVE
print("Deletando com o remove")
matriz_notas.remove(["José"])
print(matriz_notas)

# INSERT
print("Adicionando com insert")
matriz_notas.insert(0, ["Matheus", 6.8])
print(matriz_notas)

# MUDANDO UM VALOR NA MATRIZ
print("Mudando um valor na matriz")
matriz_notas[1] = ["João" , 9.0]
matriz_notas[0][0] = "Matheus Casilas"
matriz_notas[0][1] = 6.9
print(matriz_notas, type(matriz_notas), len(matriz_notas))

print("Mostrando os valores da matriz com um for alinhado")
for registro in matriz_notas:
    for dado in registro:
        print(dado)

for i in range(len(matriz_notas)):
    for j in range(len(matriz_notas)):
        print(matriz_notas[i][j])

print("Mostrando os valores da matriz com um for só")
for indice, valor in matriz_notas:
    print (indice, valor)

# for a in matriz_notas:
#     print(a[0], matriz_notas[1])

#-------------------------------------------------------------------------------------------------






