def carregarPerguntas():
    perguntas = []
    with open('perguntas.txt', 'r') as arquivo:
        for linha in arquivo:
            perguntas.append(linha.strip())
    return perguntas

perguntas = carregarPerguntas()
print(perguntas)