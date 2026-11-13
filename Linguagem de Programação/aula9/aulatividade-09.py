# dicionário (estrutura de dados heterogeneo)
# o dicionário é uma estrutura de dados que trabalha com pares de chaves e valores. Diferentemente das listas, que usavam índices numéricos para acessar os elementos, nos dicionários utilizamos chaves.

#----------------------------------------------

#Criando um dicionário e consultando-o
aluno_1 = { "nome":  "Cleber", "media": 7.5 }
print(aluno_1["nome"])
print(aluno_1["media"])

#Alterando informações
aluno_1["media"] = 10
print(aluno_1["media"])

#Adicionando informações (quando não tem a informação ele cria)
aluno_1["curso"] = "ADS"
print(aluno_1)

#Excluindo informações
del aluno_1["curso"]
print(aluno_1)

#----------------------------------------------

#Dicionário de dicionários
alunos = { 
    1: {"nome": "Cleber", "media": 7.5},
    2: {"nome": "Maria", "media": 9.5},
    3: {"nome": "Sandro", "media": 7.0}          
}

#Consultando
print(alunos[2]["nome"]) #O 2 representa o valor da CHAVE e NAO o valor do INDICE

#Alterando um item no dicionário
alunos[1]["media"] = 8.75
print(alunos)

#Adicionando um novo item
alunos[4] = {"nome": "Igor", "media": 10}
print(alunos)

#Excluindo um item
del alunos[3]
print(alunos)

#----------------------------------------------

#Lista de dicionários
lista_alunos = [
    {"nome": "Cleber", "media": 7.5},
    {"nome": "Maria", "media": 9.5},
    {"nome": "Sandro", "media": 7.5}
]
print(lista_alunos[0]["nome"]) #Aqui o 0 já representa um índice

