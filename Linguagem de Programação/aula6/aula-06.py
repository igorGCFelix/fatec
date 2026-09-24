# match - case -> tipo o switch case do C
opcao_Menu = int(input("Opção? "))
match opcao_Menu:
    case 1:
        print("Opção 1")
    case 2:
        print("Opção 2")
    case 3:
        print("Opção 3")
    case _:
        print("Opção inválida")