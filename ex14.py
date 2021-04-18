#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

#Resolução.

cel = float(input("digite grau: "))
fire = ((cel * 9)/5) + 32
print(f"Você digitou: {cel} \nGrau celsius: {cel} \nGrau convertido em Fahrenheit é: {fire}")