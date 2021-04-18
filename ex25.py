#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#Resolução.


nome = str(input("Digite seu nome: ")).strip()
nome2 = "SILVA" in nome.upper()
if nome2:
    print(f"O {nome} Tem silva")
else:
    print("Não tem Silva")