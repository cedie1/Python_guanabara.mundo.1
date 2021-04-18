#faça um algoritimo que leia o preço de produto e mostre seu novo preço, com 5% de desconto.

#Resolução

preco = float(input("Digite o valor da peça: "))
valor_final = preco - (5/100)* preco
print(f"Com o desconto de 5% o valore ficará R${ valor_final}")