#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#resolução.

km_viagem = int(input("Digite quantos KM tem sua viagem: "))

print(f"O valor da viagem para até 200 KM o valor é de  R$ 0,50 por KM\nPara viagem acima de 200 KM o valor é de R$ 0,45 por KM")
print(f"Sua viagem é de {km_viagem} KM")
if km_viagem <= 200:
    km_viagem = 0.50 * km_viagem
    print(f"o valor da sua viagem é de R$ {km_viagem:.2f}")
else:
    km_viagem = 0.45 * km_viagem
    print(f"o valor da sua viagem é de R$ {km_viagem:.2f}")
print("Obrigado e volte sempre ")