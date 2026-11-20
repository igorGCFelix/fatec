#nome.split(sep=None, maxsplit=-1)
    #sep = string que vai ser usada como separador (vírgula, hífen, espaço)
    #maxsplit = número que limita a quantidade de divisoes que podem ser feitas
    
    #nome: 'igor gonçalves de camargo felix'
    #nome: ['igor' 'gonçalves' 'de' 'camargo' 'felix']
    #print(nome.split())
#dica do mestre sobrino: split(), title(), upper()    

#exercicio 1 --------------------------------------------
def receber_nome(nome):
    #pegando a inicial do primeiro nome
    nome = nome.upper()
    inicialPrimeiroNome=nome[0]
    
    #pegando o ultimo nome
    vetorNome=nome.split()
    sobrenome=vetorNome[len(vetorNome)-1]
    
    #printando ne pae
    print(f"{sobrenome}, {inicialPrimeiroNome}.")
    
nome=input("Digite o seu nome completo: ")
receber_nome(nome)

#exercicio 2 --------------------------------------------
senhaCerta="igorBonito123"
a=False
b=1
while not a:
    senha=input("Digite a senha: \n")
    if senha==senhaCerta:
        print("🎉 Acesso permitido 🎉")
        a=True
    else:
        if b==3:
            print("🫩. Você estourou o limite de tentativas 🫩")
            a=True
        else: 
            b=b+1
            print(f"⚠️. Senha incorreta! Tente novamente... (Você tem mais {4-b} tentativa(s)) ⚠️")

#exercicio 3 --------------------------------------------
#1. definir e confirmar a senha
#2. A senha deve ter exatamente 8 caracteres (ao menos 1 maíusculo, ao menos 1 minúsculo, 1 numero e 1 caractere especial)
caracteresEspeciais=[ "@", "#", "$", "%", "&", "*", "+", "-", "/", "=", "?", "!", "~", "^", "_", "|", "©", "®", "™", "§", "•", "—", "…", "«", "»", "€", "£", "¥", "±", "≠", "≤", "≥", "∞", "½", "²", "→", "←", "↑","↓", "★", "☆", "♥", "✓"]

def verificarCaracteresEspeciais(senha):
    validarCaracteresEspeciais=False
    quantidadeCaracteresEspeciais=0
    for letra in senha:
        if letra in caracteresEspeciais:
            quantidadeCaracteresEspeciais=quantidadeCaracteresEspeciais+1
            
    if quantidadeCaracteresEspeciais>1: print("Você só pode usar 1 caractere especial!")
    elif quantidadeCaracteresEspeciais==0: print("Você precisa usar 1 caractere especial! E apenas 1!")
    else: validarCaracteresEspeciais=True
    
    return validarCaracteresEspeciais

def verificarLetraMaisculaMinuscula(senha):
    validarLetraMaiuscula=False
    validarLetraMinuscula=False
    for letra in senha:
        if letra.isupper(): validarLetraMaiuscula=True
        #tenho que fazer o islower() também, pq se não ele vai validar o caractere especial como se fosse minúsculo
        elif letra.islower(): validarLetraMinuscula=True
        
    if not validarLetraMaiuscula: print("Senha inválida! A senha deve possuir pelo menos 1 caractere maísculo.")
    if not validarLetraMinuscula: print("Senha inválida! A senha deve possuir pelo menos 1 caractere minúsculo.")
    
    return validarLetraMaiuscula, validarLetraMinuscula

def verificarNumero(senha):
    validarNumero=False
    quantidadeNumero=0
    for letra in senha:
        if letra.isdigit(): quantidadeNumero=quantidadeNumero+1

    if quantidadeNumero>1: print("Senha inválida! A senha deve possuir somente 1 número!")
    elif quantidadeNumero==0: print("Senha inválida! A senha deve possuir 1 número. E apenas 1 número!")
    else: validarNumero=True
    
    return validarNumero

a=False
print("--- Crie sua senha ---")

while not a:
    senha=input("Digite sua senha: \n")
    confirmarSenha=input("Confirme sua senha: \n")
    
    tem_maiuscula, tem_minuscula = verificarLetraMaisculaMinuscula(senha)
    
    if senha==confirmarSenha:
        if verificarCaracteresEspeciais(senha) and tem_maiuscula and tem_minuscula and verificarNumero(senha):
            print("Senha válida")
            a=True
        else:
            print("As condições não foram atendidas!")
    else:
        print("As duas senhas são diferentes, certifique-se de digitar a mesma senha duas vezes!")