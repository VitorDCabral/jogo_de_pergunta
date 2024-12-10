perguntas = (("Quantos elementos existem na tabela periodica?: "),
             ("Qual animal põe o maior ovo do mundo?: "),
             ("Qual é o gás mais abundante no planeta Terra?: "),
             ("Quantos ossos existem no corpo humano?: "),
             ("Qual é o planeta mais quente no sistema solar?: "))

opcoes = (("A. 116", "B .117", "C. 118", "D. 119"),
          ("A. Baleia", "B. Crocodilo", "C. Elefante", "D. Avestruz"),
          ("A. Nitrogenio", "B. Oxigenio", "C. Dioxio de Carbono", "D. Hidrogenio"),
          ("A. 206", "B. 207", "C. 208", "D. 209"),
          ("A. Mercurio", "B. Venus", "C. Terra", "D. Marte"))

respostas = ("C", "D", "A", "A", "B")
chutes = []
pontos = 0
num_perguntas = 0

for pergunta in perguntas:
    print("----------------------")
    print(pergunta)
    for opcoe in opcoes[num_perguntas]:
        print(opcoe)
        
    chute = input("Coloque(A, B, C, D): ").upper()
    chutes.append(chute)
    if chute == respostas[num_perguntas]:
        pontos += 1
        print("Correto")
    else:
        print("Incorreto")
        print(f"{respostas[num_perguntas]} é a resposta correta")    
    num_perguntas += 1 

print("----------------------")
print("      RESULTADOS      ")
print("----------------------")

print("respostas: ", end="")
for resposta in respostas:
    print(resposta, end=" ")
print()

print("chutes: ", end="")
for chute in chutes:
    print(chute, end=" ")
print()        

ponto = int(pontos / len(perguntas) * 100)
print(f"Sua pontuação foi: {ponto}%")        