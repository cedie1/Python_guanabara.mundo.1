
'''
Escreva um programa que pergunte a quantidade de Km percorridos
por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

Resolução
'''


qtpercorrido = float(input("Quantos Km você percorreu? "))
dia_alug = int(input("Por quantos dias foi alugado o veiculo? "))
diaria = 60 * dia_alug
km = 0.15 * qtpercorrido
total = diaria + km
print(f"Você percorreu {qtpercorrido} KM totalizando o valor de: R$ {km:.2f}"
      f" \nVocê alugou o veiculo por: {dia_alug} dias totalizando o valor de: R$ {diaria:.2f}"
      f" \nO cliente deve pagar: R$ {total:.2f}")