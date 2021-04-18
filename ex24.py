# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

#Resolução.

"""
cidade = str(input("digite o nome de uma cidade: ")).strip()
cid = cidade[:5] .upper() == "SANTO"
print(cid)

"""


cidade = str(input("digite o nome de uma cidade: ")).strip()
cid = cidade[:5] .upper() == "SANTO"
if cid:
    print(f"O inicio é santo")
else:
    print(f"Não inicia com santo")