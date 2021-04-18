'''
Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80 Km / h, mostre uma
mensagem dizendo que ele foi multado.A multa vai custar R$7,00 por  cada  Km  acima do limite.

resolução.
'''

velocidade = int(input("Digite a velocidade do seu carro: "))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(
        f"Você esta {velocidade} KM/H \nVocê foi multado em R$ {multa:.2f} pois estava acima da velocidade da rodovia")
else:
    print("Sua velocidade está ok, boa viagem!")

print("-----  FIM  ----")