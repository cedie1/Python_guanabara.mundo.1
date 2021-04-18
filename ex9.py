#faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada.

#Resolução.
from time import sleep
num = int(input('Tabuada do numero: '))

for n in range(11):
     print(f"{num} x {n} = {num*n}")
     sleep(1)