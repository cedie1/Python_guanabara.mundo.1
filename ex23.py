#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Resolução.

num = int(input("Digite um numero: "))
num1 = num // 1 % 10
num2 = num // 10 % 10
num3 = num // 100 % 10
num4 = num // 1000 % 10
result = f"O numero digitado foi: {num}\nÉ uma unidade : {num1} \nÉ uma dezena: {num2} \nÉ uma centena: {num3} \nÉ uma milhar: {num4}"
print(result)