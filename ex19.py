#um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que ajude ele, lendo nome deles e escrevendo o nome escolhido.

#resolução

import random
nomes = input("digite quatro nomes separados por virgula: ").split(",")
sorteio = random.randint(1, 4)
string = f"Alunos{nomes} \nAluno sorteado é:{nomes[sorteio - 1]} numero de sorteio {sorteio}"
print(f"o numero sorteado foi: n° {sorteio}")
print(string)