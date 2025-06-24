#Questão 1: 
'''matriz = []

linhas = int(input("número de linhas da matriz: "))
colunas = int(input("número de colunas: "))

for i in range(linhas):
    linhas_matriz = []
    for j in range(colunas):
        if i < j:
            linhas_matriz.append((2 * i + 7 * j + 2))
        elif i == j:
            linhas_matriz.append((3 * (i**2) + 1))
        else:
            linhas_matriz.append(4 * (i**3) + 5 * (j**2))
    matriz.append(linhas_matriz) 


print(f"\nMatriz {linhas} x {colunas}")
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end=" ")
    print(" ")'''


#Questão 2: 
aprovados = 0
gabarito = []
print("Qual o gabarito da prova? ")
for i in range(5):
    resposta_gabarito = input(f"Questão {i + 1}: ")
    gabarito.append(resposta_gabarito)


for a in range(5):
    aluno = a + 1
    print(f"\nInforme as respostas do aluno {aluno}")
    
    respostas = []
    for b in range(5):
        resposta_aluno = input(f"Questão {b + 1}: ")
        respostas.append(resposta_aluno)

    questoes_certas = 0
    for c in range(5):
        if respostas[c] == gabarito[c]:
            questoes_certas += 1
    
    nota_fim = questoes_certas * 2.0
    
    if nota_fim >= 7:
        aprovados += 1
print("O percentual de aprovação é de ", ((aprovados/5) * 100))