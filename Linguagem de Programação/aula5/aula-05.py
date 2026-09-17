#função-> facilita o uso de tarefas repetitivas

#encapsular a responsabilidade daquela funcionalidade
#parametros que coloca-se no parenteses
#chamada para função tem os argumetos
# a função recebe os argumentos nos parametros

#a exibição n deveria ficar a cargo da função, deve ficar com quem chamou a função -a nao ser que seja focadamente para exibir algo

#parametro default(padrao) -> estabelece um valor padrao caso nao receba os argumentos do usuário: 
# def somar_numeros(n1=0, n2=0):
#   return n1, n2
# print(somar_numeros()) -> vai retornar o 0

def somar_numeros(n1 = 0,n2 = 0):
    return n1 + n2

r = somar_numeros(1,2)
print(r)
