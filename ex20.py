#o mesmo professor do desafio anterior quer sortear a ordem de  apresentação de trabalhos dos alunos. faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

#Resolução.

import random
nomes = input("digite quatro nomes separados por virgula: ").split(",")

random.shuffle(nomes)

string = f"{nomes}"
print(string)