#faça um algoritimo que leia o salario de
#um funcionario e mostre se novo salario com 15% de aumento.

#resolução.

saliro = float(input("digite seu salario: "))
aumento = (15/100) * saliro
valor_final = saliro + aumento
print(f"Seu salrio aumento para {valor_final}")