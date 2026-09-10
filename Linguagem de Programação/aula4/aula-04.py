# array -> uma variável especial que guarda mais de um valor por variavel
# no python o array n possui uma tipagem homogenea, igual do C
# vetor -> lista
#  CRUD -> Create Read Update Delete
# array -> índice -> 0,1,2,3,4,5... -> posição do array

# os dois funcionam
# mas sempre é melhor trabalhar com listas paralelas
# lista1 = [8.5, 3.5, 10]
# lista2 = ["José", 3.5, True]

# lista paralelas -> o mesmo indice nos dois -> Café - 25 -> [índice 0]
# listaProdutos = ["Café", "Arroz", "Batata"]
# listaPrecos = [25, 30, 15]

# listaAmigos = []
listaAmigos = ["Rafael", "Joao Luca", "Guilherme", "Lucas", "Andrews"]
# print(listaAmigos)
# print("Tipo: ", type(listaAmigos))
# print("Tamanho: ", len(listaAmigos))

# for item in range(len(listaAmigos)): 
#     print(item)
#     # mostra o índice

    
# for item in listaAmigos: 
#     print(item)
#     #lista o array

 #adiciona um elemento no final da lista
listaAmigos.append("Flávio")
#adiciona um elemento falando onde irá acrecentar no índice
listaAmigos.insert(0, "Thiago")

# substituição de valor
listaAmigos[5] = "Nicolas"

#removendo um elemento no final da lista
listaAmigos.pop()
#removendo um elemento falando o índice
listaAmigos.pop(0)
# remove o primeiro
listaAmigos.remove("Rafael")

print(listaAmigos)

# organiza os elementos da própria lista original em ordem crescente ou alfabética de forma permanente
listaAmigos.sort()

# limpando a lista
# listaAmigos.clear()

# excluir a variavel
# del listaAmigos

