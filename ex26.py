#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

#Resolução.


frase = str(input("Digite algo: ")).strip().upper()
frase2 = frase.count("A")
frase3 = frase.find("A")+1
frase4 = frase.rfind("A")+1

result = f"Quantas letras A tem: {frase2} \nA primeira letra A esta na posição: {frase3} \nA ultima letra A esta na posição: {frase4}  "
print(result)