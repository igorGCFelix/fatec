# Exercício 1 ------------------------------------------------------------- 
# a=False
# while not a:
#     try:
#         valor_real = float(input("Digite o valor em reais: "))
#         valor_dolar = float(input("Digite o valor da cotação do dólar: "))
#         a=True
#     except ValueError:
#         print("Certifique-se de digitar somente números!")
    
    
# conversao_dolar = valor_real/valor_dolar
# print(f"{valor_real} Reais é equivalente à {conversao_dolar} Dólares")

# Exercício 2 ------------------------------------------------------------- 
# def conversao_dolar(real, dolar):
#     valor_dolar=real/dolar
#     return valor_dolar

# a=False
# while not a:
#     try:
#         valor_real = float(input("Digite o valor em reais: "))
#         valor_dolar = float(input("Digite o valor da cotação do dólar: "))
#         a=True
#     except ValueError:
#         print("Certifique-se de digitar somente números!")

# dolar_convertido = conversao_dolar(valor_real,valor_dolar)

# print(f"{valor_real} Reais é equivalente à {dolar_convertido} Dólares")

# Exercício 3 ------------------------------------------------------------- 
# def tratar_string(string): 
#     string = (string.strip()).upper()
#     return string
    

# def calcular_valor_total(tempo_permanencia_min, valor_hora, valor_extra, valor_diaria):
#     tempo_permanencia_horas=tempo_permanencia_min/60
    
#     if tempo_permanencia_horas <= 0.083:
#         total_a_ser_pago = 0
#     elif tempo_permanencia_horas == 1:
#         total_a_ser_pago = valor_hora
#     elif tempo_permanencia_horas > 1:
#         parte_inteira = int(tempo_permanencia_horas) 
#         parte_decimal = tempo_permanencia_horas-parte_inteira
    
#         if parte_decimal>0:
#             total_a_ser_pago = valor_hora + valor_extra*((parte_inteira-1)+1)
#         else:
#             total_a_ser_pago = valor_hora + valor_extra*parte_inteira
#     elif tempo_permanencia_horas>=8:
#         total_a_ser_pago=valor_diaria
        
#     return total_a_ser_pago

# a=False
# while not a:
#     try:
#         tempo_permanencia_min = int(input('Digite o tempo de permanência do veículo em minutos: '))
#         if tempo_permanencia_min >= 0:
#             b=False
#             while not b:
#                 tipo_veiculo = input("Digite o tipo de veículo (Carro ou Moto): ")
#                 tipo_veiculo = tratar_string(tipo_veiculo)
#                 b=True if tipo_veiculo == "CARRO" or tipo_veiculo == "MOTO" else print("Escolha o tipo de veículo entre as opções fornecidas: CARRO ou MOTO")
#             a=True 
        
#     except ValueError:
#         print("Certifique-se de inserir os valores corretamente")


# if tipo_veiculo == "CARRO": print(calcular_valor_total(tempo_permanencia_min,15,7.5,50))     
# elif tipo_veiculo == "MOTO": print(calcular_valor_total(tempo_permanencia_min,10,5,35))

# Exercício 4 ------------------------------------------------------------- 
quantidade = int(input("Digite a quantidade de termos a serem exibidos: "))
fibonacci = []
a, b = 0, 1

for i in range(quantidade):
    fibonacci.append(a)
    a, b = b, a + b

for i in range(quantidade):
    print(f"Termo {i+1}: {fibonacci[i]}")

# Exercício 5 ------------------------------------------------------------- 
