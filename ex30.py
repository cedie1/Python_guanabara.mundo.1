#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#resolução.

n = int(input("Digite um numero: "))
resulta = n % 2
if resulta == 0:

    print(f"O numero {n} é par ")
else:
    print(f"O numero {n} é impar")