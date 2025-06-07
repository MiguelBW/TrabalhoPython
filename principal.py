import random
def quizz(nome, pontInicio, multInicio, nPerguntas):
    perguntasFile = r'dados\perguntas.txt'
    respostasFile = r'dados\respostas.txt'
    try:
        with open(perguntasFile, 'r', encoding='utf-8') as perguntasF, open(respostasFile, 'r', encoding='utf-8') as respostasF:
            arrPerguntas = perguntasF.readlines()
            arrRespostas = respostasF.readlines()

        rdmPerguntas = random.sample(range(1,len(arrPerguntas)+1),nPerguntas)
        opcoes = ['A','B','C','D']
        opcaoCorreta = ''
        acertos = 0
        falhas = 0
        multiplicador = multInicio
        multAcerto = 0.10
        multFalha = -0.20
        valorPergunta = 1000.0
        pontuacao = pontInicio
        i = 0
        for x  in rdmPerguntas:
            print(f'\n\033[94m︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽︽\033[0m')
            print(f'\033[94mJOGADOR: \033[91m {nome}')
            print(f'\033[94mPergunta: {i+1} de {nPerguntas}\033[0m\033[92m   Acertou:{acertos}\033[0m\033[91m   Falhou:{falhas}\033[0m',end='')
            print(f'\n\033[94mMultiplicador: {multiplicador:.2f}x\n\033[0m{arrPerguntas[x-1]}',end='')

            y=0
            while y < len(arrRespostas):
                if x == int(arrRespostas[y]):
                    for j in range(1, 5):
                        linhaResposta = arrRespostas[y + j].rstrip()
                        print(f'{opcoes[j-1]} - {linhaResposta[:-1]}',end='\n')
                        if linhaResposta.endswith('#'):
                            opcaoCorreta = opcoes[j-1]
                y+=5
            if input().strip().upper() == opcaoCorreta:
                print(f'\033[92mCORRETO + {(valorPergunta * multiplicador):.0f} 🗿\033[0m')
                acertos += 1
                pontuacao += (valorPergunta * multiplicador)
                multiplicador += multAcerto
            else:
                print(f'\033[91mINCORRETO 🤣 {multFalha}x\033[0m\n\033[92mresposta correta: {opcaoCorreta}\033[0m')
                falhas += 1
                multiplicador += multFalha
                
            print(f'\033[94m︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾︾\033[0m\n')
            i += 1
        print(f'\033[94mMultiplicador: {multiplicador:.2f}x\033[0m  \033[92mPONTUAÇÃO: {pontuacao:.0f}\033[0m',end='\n')
        print(f'\033[94mDe {nPerguntas} Pergunta(s)\033[0m\033[92m   Acertou:{acertos}\033[0m\033[91m   Falhou:{falhas}\033[0m',end='\n')
        return(pontuacao, multiplicador)
    except FileNotFoundError as e:
        print(f'erro: {e}')
        return(pontFinal,multFinal)
    
print(f'\nO multiplicador começa em \033[94m1.00x\033[0m após cada acerto aumenta \033[92m+0.10\033[0m a cada falha diminui \033[91m-0.20\033[0m\nO Jogador com maior pontuação vence, \033[92mBoa Sorte!\033[0m')
jogadores = {}
qtdJogadores = int(input(f'\033[94mQuantas pessoas irão jogar? \033[0m'))

try:
    perguntasFile = r'dados\perguntas.txt'
    with open(perguntasFile, 'r', encoding='utf-8') as perguntasF:
        arrPerguntas = perguntasF.readlines()
        nPerguntas = int(input(f'\033[94mQuantas perguntas de \033[91m{len(arrPerguntas)}\033[94m desejam responder? \033[0m'))
except FileNotFoundError as e:
    print(f'erro: {e}')
    quit()

for x in range(qtdJogadores):
    nome = input(f'\033[94mPlayer \033[91m{x+1}\033[94m Insira seu username: \033[0m')
    jogadores[nome] = {'pontuacao': 0.0, 'multiplicador': 1.0}

for nome in jogadores:
    pont, mult = jogadores[nome]["pontuacao"], jogadores[nome]["multiplicador"]
    pontFinal, multFinal = quizz(nome, pont, mult, nPerguntas)
    jogadores[nome]["pontuacao"] = pontFinal
    jogadores[nome]["multiplicador"] = multFinal

print("\n\033[95mRESULTADOS FINAIS:\033[0m")
for nome, dados in jogadores.items():
    print(f'\033[91m{nome} : \033[92m{dados["pontuacao"]:.0f} pontos\033[0m | \033[94m{dados["multiplicador"]:.2f}x\033[0m')