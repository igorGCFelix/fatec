def adicionar_nota(nome, nota): 
    nomes.append(nome)
    notas.append(nota)

def listar_notas(nomes, notas): 
    print("--- Lista ---")
    for item in range(len(nomes)):
        print(f"Aluno: {nomes[item]}, Média: {notas[item]}, Índice: {item}")

def excluir_nota(indice):
    notas.pop(indice)
    nomes.pop(indice)

def alterar_nota(indice, nome, nota):
    nomes[indice] = nome
    notas[indice] = nota

def press_continuar():
    input("Pressione Enter para iniciar...")

nomes = []
notas = []

print("--- Exercício 3 ---")

input("Pressione Enter para iniciar...")

adicionar_nota("João", 7.5)
adicionar_nota("Maria Farah", 8.5)
adicionar_nota("Henrique Lima", 7)
adicionar_nota("Claudio José", 5.5)
listar_notas(nomes, notas)

press_continuar()

alterar_nota(1, "João Silva", 6.5)
listar_notas(nomes, notas)

press_continuar()

excluir_nota(3)
listar_notas(nomes, notas)


