#faça um programa que leia o comprimento do cateto oposto e do adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

#Resolução.

import math

cateto_op = float(input("digite o cateto oposto: "))
cateto_adj = float(input("cateto adjancente: "))
soma_catetos = cateto_op**2 + cateto_adj**2
resultado_hipotenusa = math.sqrt(soma_catetos)

print(f"O resultado da hipotenusa é: {resultado_hipotenusa: .2f}")
