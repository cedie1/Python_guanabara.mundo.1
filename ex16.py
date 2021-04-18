#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira.

#Resolução.

import math

n1 = float(input("Digite um numero fracionado: "))
n2 = math.trunc(n1)
print(f"O numero digitado foi: {n1} \nSua porção inteira é: {n2}")