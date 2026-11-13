#-----------------------------------------------------------------
# import json

# arquivoSisNotas = open("alunos.json", "r", encoding="utf-8")
# alunos = json.load(arquivoSisNotas)
# arquivoSisNotas.close()

# print(alunos["2"]["media"])

#-----------------------------------------------------------------

# import json

# with open("alunos.json", "r", encoding="utf-8") as arquivoSisNotas:
#     alunos = json.load(arquivoSisNotas)

# print(alunos)

#-----------------------------------------------------------------

import json

alunos = {
    1: {"nome": "Cleber", "media": 7.5},
    2: {"nome": "Maria", "media": 9.5},
    3: {"nome": "Sandro", "media": 7.5}
}

with open("alunos.json", "w", encoding="utf-8") as arquivoSisNotas: #só executa o código quando o arquivo estiver aberto, assegurando o fechamento quando o bloco for concluído
    json.dump(alunos, arquivoSisNotas, ensure_ascii=False, indent=4)