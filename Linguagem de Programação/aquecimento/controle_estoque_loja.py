
def menu():
    i=0
    while i<1:
        opcao=int(input("Escolhe uma das opções: \n [1] Vender \n [2] Repor \n [3] Excluir \n [4] Sair \n [5] Mostrar Estoque \n [6] Limpar \n"))
        
        match opcao:
            case 1:
                item = input("Digite o item que quer vender: \n")
                quantidadeItem = int(input("Digite a quantidade de produtos que quer vender: \n"))
                
                acharIndice(item)
                vender(quantidadeItem)
            case 2:
                item = input("Digite o item que você quer repor: \n")
                quantidadeAddEstoque = int(input("Digite a quantidade que deseja adicionar: \n"))
                
                acharIndice(item)
                repor(quantidadeAddEstoque)
            case 3:
                item = input("Digite o produto que deseja remover do estoque: \n")
                excluir()
            case 4:
                i=1
            case 5:
                mostrarEstoque()
            case 6:
                print("\033[H\033[J", end="")
            case _:
                print("Valor inválido")
                
def acharIndice(item):
    try:
        indice = produtos.index(item)
        return indice
    except ValueError:
        print("Produto não cadastrado no estoque.")
        return None

def vender(indice, quantidadeItem):
    tamanhoEstoque = quantidades[indice]
    
    if tamanhoEstoque<quantidadeItem:
        print("A quantidade de produtos requerida excede a quantidade armazenada no estoque!")
    else: 
        quantidades[indice] = quantidades[indice] - quantidadeItem
        
def mostrarEstoque():
    for i in range(len(produtos)):
        print(f"Produto: {produtos[i]}, Preço: {precos[i]}, Quantidade: {quantidades[i]} \n")

def repor(indice, quantidadeAddEstoque):
    # vai pedir o indice e o quanto quer adicionar ao estoque
    quantidades[indice] = quantidades[indice] + quantidadeAddEstoque
    
def excluir(indice, item):
    # remover produto
    opcao = input(f"Deseja realmente exluir o produto {produtos[indice]} (S/N)? ")
    if opcao.upper()=="S": 
        produtos.pop(indice)
        precos.pop(indice)
        quantidades.pop(indice)
    elif opcao.upper()=="N":
        print("Operação cancelada!")
    else:
        print("Valor inválido!")
        
    

produtos = ["Caneta", "Caderno", "Lápis", "Borracha", "Mochila", "Régua", "Tesoura", "Cola"]
precos = [2.5, 15.0, 1.5, 1.0, 89.9, 3.5, 7.0, 4.5]
quantidades = [100, 40, 150, 80, 12, 60, 25, 0]

menu()
