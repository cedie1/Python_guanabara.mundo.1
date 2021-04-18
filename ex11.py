#faça um programa que leia largura ea altura de uma parede em metros e calcule sua área ea quantidade de tinta necessaria para pinta-la sabendo que cada litro de tinta pinta uma área de 2m²

#resolução.

alt = float(input("digite a altura em metros: "))
larg = float(input("digite a largura em metros: "))
area = alt * larg
tinta = area / 2
print(f"sera necessario: {tinta :.2f} litros")