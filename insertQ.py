def lerPerguntas():
    perguntasFile = r'dados2\perguntas.txt'
    with open(perguntasFile, 'r', encoding='utf-8') as perguntasF:
        return(perguntasF.readlines())
    
def lerRespostas():
    respostasFile = r'dados2\respostas.txt'
    with open(respostasFile, 'r', encoding='utf-8') as respostasF:
        return(respostasF.readlines())



def listarPerguntas():
        arrPerguntas = lerPerguntas()
        x = 0
        while x < len(arrPerguntas):
            print(f'{x+1} - {arrPerguntas[x]}',end="")
            x += 1
        
def removerPergunta():
    perguntasFile = r'dados2\perguntas.txt'
    respostasFile = r'dados2\respostas.txt'
    
    arrPerguntas = lerPerguntas()
    arrRespostas = lerRespostas()
    num = int(input(f'Insira o nº da pergunta que deseja remover?'))
    perguntaRemovida = arrPerguntas.pop(num-1)

    print(f'{perguntaRemovida}')
    y=0
    while y < len(arrRespostas):
        if (num-1) == int(arrRespostas[y]):
            for j in range(0, 5):
                arrRespostas.pop(y+j)
                print
        else:
            y+=5
            
    with open(perguntasFile, 'w', encoding='utf-8') as perguntasF:
        perguntasF.writelines(arrPerguntas)
        print(f'{perguntaRemovida}')
    with open(respostasFile, 'w', encoding='utf-8') as respostasF:
        respostasF.writelines(arrRespostas)
        
def menu():
    while True:
        print("\n====== MENU ======")
        print("1. Listar Perguntas")
        print("2. Remover pergunta")
        print("0. Sair")
        print("==================")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                listarPerguntas()
            case "2":
                removerPergunta()
            case "0":
                print('A Sair...')
                break
            case _:
                print("Opção inválida. Tente novamente.")

menu()