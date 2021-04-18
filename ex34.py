'''
Escreva um programa que pergunte o salário de um funcionário e
calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
resolução.
'''
salario = float(input("digite seu salario: "))

if salario >= 1250.00:
    aumento10 = (10/100) * salario
    print(f"O salario de {salario :.2f} com o aumentou de 10% resultou em R${salario + aumento10 :.2f}")
else:
    aumento15 = (15/100) * salario
    print(f"O salario  de R$ {salario :.2f} com o aumento de 15% resultou em R${salario + aumento15 :.2f}")
