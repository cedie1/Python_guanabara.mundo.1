#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#resolução.

nome_completo = str(input("Digite seu nome completo: ")).strip().upper()
lista_nomes = nome_completo.split()
prmeiro_nome = lista_nomes[0]
ultimo_nome = lista_nomes[-1]

print(f"Seu primeiro nome é: {prmeiro_nome} \nSeu ultimo nome é: {ultimo_nome}")