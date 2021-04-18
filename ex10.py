#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar .

#considerar uss 1.oo  = r$ 3,27

real = float(input("digite quanto você tem: "))
conversao = real / 3.27

print(f"Você tem R$ {real} posso comprar US$ {conversao :.2f}")