n1 = float(input("digite a nota: "))
n2 = float(input("digite a segunda nota: "))
m = (n1 + n2)/2
print(f"A sua média foi {m}")
if m >= 6.0:
    print(f"Parabéns Você foi Aprovado")
else:
    print(f"Infelizmente você foi reprovado !")

print(f"---FIM----")

#exemlo de condicionais



nome = str(input("Digite seu nome: ")).strip().upper()
if nome =="CELSO":
    print(f"Bem vindo: {nome}")
else:
    print(f" usuario {nome} inexistente")

print(f"---FIM----")