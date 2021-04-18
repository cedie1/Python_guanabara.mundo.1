# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

#resolução.

import random
from time import sleep
print("--=--" * 20)
print("Vou sortear um número entre 0 e 5. tente advinhar")
print("--=--" * 20)

nu = int(input("Digite um numero de 0 a 5: "))

sorteio = random.randint(0, 5)

print(f"Processando... ")
sleep(3)

print(f"O numero Sorteado foi: {sorteio} ")

if nu == sorteio:
    print(f"Parabens você acertou: ")
else:
    print("Você errou. Tente novamente!")

print("-----FIM----")