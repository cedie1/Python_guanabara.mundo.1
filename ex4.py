#dissecando variavel

#Resolução:

n1 = (input("Digite algo: "))
print("O tipo primitivo desse valor é",type(n1))
print("Só tem espaços ? ", n1.isspace())
print("É um número ? ", n1.isnumeric())
print("É alfabetico ? ", n1.isalpha())
print("É alfanúmerico", n1.isalnum())
print("Só tem maiúsculas ?",n1.isupper())
print("Só tem minúsculas ? ", n1.islower())
print("Está capitalizada? ", n1.istitle())
