'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

resolução
'''

nome = str(input("Digite seu nome completo: ")).strip()
string = nome.upper()
string2 = nome.lower()
string3 = len(nome) - nome.count(" ")
string4 = nome.find(" ")

todas_strings = f"Seu nome maiúsculo: {string} \nSeu nome minúsculo: {string2} \nQuantdade de caracters: {string3} \nSeu nome contém: {string4} "

print(todas_strings)


#celso diego pereira

#Curso em Video Python

#Aprenda Python

