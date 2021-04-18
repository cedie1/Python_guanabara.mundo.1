#faça um programa que leia um angulo qualquer e mostre na tela seno cosseno e tangente desse ano

#Resolução.

import math

angulo = float(input("Digite o valor de um  angulo: "))
angulo = math.radians(angulo)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tange = math.tan(angulo)

print(f"Você digitou: {angulo:.2f} \nO valor do seno: {seno:.2f} \nO valor do cosseno: {cosseno:.2f}\nO valor da tangente:{tange:.2f}")