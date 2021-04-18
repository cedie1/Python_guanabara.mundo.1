#escreva um programa que leia um valor em metros e exiba convertido em centimetro e milimetros.

#Resolução.

n1 = int(input("Digite um numero: "))
print(f"O numero digitado equivale a: {n1}MT(s) \nQue equivale: {n1*100}CM \nCujo o valor MM é: {n1*1000}")

#complemento.

'''
medida = float(input('Uma distancia em metros: '))
mm = medida * 1000
cm = medida * 100
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('a media  de  {}m coresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
'''