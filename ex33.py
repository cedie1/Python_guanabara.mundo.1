#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#resolução.

"""
complemento 

numeros = input("Digite numereos sepados por virgula: ").split(",")
maior = max(numeros)
menor = min(numeros)
print(f"O maior numero é {maior}\nO menor numero é {menor} ")

"""

valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))
valor_3 = int(input("Digite o terceiro valor: "))

if valor_1 < valor_2 and valor_1 < valor_3:
    menor = valor_1
if valor_2 < valor_3 and valor_2 < valor_1:
     menor = valor_2
if valor_3 < valor_1 and valor_3 < valor_2:
    menor = valor_3



if valor_1 > valor_2 and valor_1 > valor_3:
    maior = valor_1
if valor_2 > valor_3 and valor_2 > valor_1:
    maior = valor_2
if valor_3 > valor_1 and valor_3 > valor_2:
    maior = valor_3

print(f"O Maior valor digitado é {maior} \nO Menor valor digitado é { menor}")