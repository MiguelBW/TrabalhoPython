import random
def quizz(nome, pontInicio, multInicio, nPerguntas):
    perguntasFile = r'dados\perguntas.txt'
    respostasFile = r'dados\respostas.txt'
    try:
        with open(perguntasFile, 'r', encoding='utf-8') as perguntasF, open(respostasFile, 'r', encoding='utf-8') as respostasF:
            arrPerguntas = perguntasF.readlines()
            arrRespostas = respostasF.readlines()

        rdmPerguntas = random.sample(range(1,len(arrPerguntas)+1),nPerguntas)
        opcoes = ['1','2','3','4']
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
            print(f'\n\033[33m╔═══════════════════════════════════════════')
            print(f'║\033[36mJOGADOR: \033[91m {nome}')
            print(f'\033[33m║\033[36mPergunta: {i+1} de {nPerguntas}\033[0m\033[92m   Acertou:{acertos}\033[0m\033[91m   Falhou:{falhas}\033[0m',end='')
            print(f'\n\033[33m║\033[36mMultiplicador: {multiplicador:.2f}x\n\033[33m║\033[0m{arrPerguntas[x-1]}',end='')

            y=0
            while y < len(arrRespostas):
                if x == int(arrRespostas[y]):
                    for j in range(1, 5):
                        linhaResposta = arrRespostas[y + j].rstrip()
                        print(f'\033[33m║\033[0m{opcoes[j-1]} - {linhaResposta[:-1]}',end='\n')
                        if linhaResposta.endswith('#'):
                            opcaoCorreta = opcoes[j-1]
                y+=5
            print('',end=' ')
            if input().strip().upper() == opcaoCorreta:
                print(f'\033[33m║\033[92mCORRETO + {(valorPergunta * multiplicador):.0f} 🗿\033[0m')
                acertos += 1
                pontuacao += (valorPergunta * multiplicador)
                multiplicador += multAcerto
            else:
                print(f'\033[33m║\033[91mINCORRETO 🤣 {multFalha}x\033[0m\n\033[33m║\033[92mresposta correta: {opcaoCorreta}\033[0m')
                falhas += 1
                multiplicador += multFalha
                
            print(f'\033[33m╠═══════════════════════════════════════════')
            i += 1
        print(f'\033[33m║\033[36mMultiplicador: {multiplicador:.2f}x\033[0m  \033[92mPONTUAÇÃO: {pontuacao:.0f}\033[0m',end='\n')
        print(f'\033[33m║\033[36mDe {nPerguntas} Pergunta(s)\033[0m\033[92m   Acertou:{acertos}\033[0m\033[91m   Falhou:{falhas}\033[0m',end='\n')
        print(f'\033[33m╚═══════════════════════════════════════════')

        return(pontuacao, multiplicador,acertos,falhas)
    except FileNotFoundError as e:
        print(f'erro: {e}')
        return(pontFinal,multFinal,acertos,falhas)
    


print(f'\nO multiplicador começa em \033[36m1.00x\033[0m após cada acerto aumenta \033[92m+0.10\033[0m a cada falha diminui \033[91m-0.20\033[0m\nO Jogador com maior pontuação vence, \033[92mBoa Sorte!\033[0m')
jogadores = {}
def qtdPerguntas():
    try:
        perguntasFile = r'dados\perguntas.txt'
        with open(perguntasFile, 'r', encoding='utf-8') as perguntasF:
            arrPerguntas = perguntasF.readlines()
            totPerguntas = len(arrPerguntas)
            while True:
                try:
                    nPerguntas = int(input(f'\033[36mQuantas perguntas de \033[91m{totPerguntas}\033[36m desejam responder? \033[0m'))
                    if nPerguntas < 0:
                        print(f'\033[91mValor não suportado\033[0m')
                    elif nPerguntas > totPerguntas:
                        print(f'\033[91mExistem apenas {totPerguntas} Perguntas\033[0m')
                    elif nPerguntas == 0:
                        print(f'\033[91mA sair...\033[0m')
                        quit()
                    else:
                        return nPerguntas
                except ValueError:
                    print(f'\033[91mPor Favor, Insira um número válido...\033[0m')
    except FileNotFoundError as e:
        print(f'erro: {e}')
        quit()

def qtdJogadores():
    while True:
        try:
            nJogadores = int(input(f'\033[36mQuantas pessoas irão jogar? \033[0m'))
            if nJogadores < 0:
                print(f'\033[91mValor não suportado\033[0m')
            elif nJogadores > 5:
                print(f'\033[91mO número máximo de jogadores é 5\033[0m')
            elif nJogadores == 0:
                print(f'\033[91mA sair...\033[0m')
                quit()
            else:
                return nJogadores
        except ValueError:
            print(f'\033[91mPor Favor, Insira um número...\033[0m')

nPerguntas = qtdPerguntas()
nJogadores = qtdJogadores()

for x in range(nJogadores):
    nome = input(f'\033[36mPlayer \033[91m{x+1}\033[36m Insira seu username: \033[0m')
    jogadores[nome] = {'pontuacao': 0.0, 'multiplicador': 1.0, 'acertos': 0, 'falhas': 0}

for nome in jogadores:
    pont, mult = jogadores[nome]['pontuacao'], jogadores[nome]['multiplicador']
    pontFinal, multFinal, acertos, falhas = quizz(nome, pont, mult, nPerguntas)
    jogadores[nome]['pontuacao'] = pontFinal
    jogadores[nome]['multiplicador'] = multFinal
    jogadores[nome]['acertos'] = acertos
    jogadores[nome]['falhas'] = falhas

jogadoresOrdenados = sorted(jogadores.items(), key=lambda item: item[1]['pontuacao'], reverse=True)
print('\n\033[33m╔════════════════════════════════════════════════════════╗')
print('║' + f'\033[95mRANKING FINAL - {nPerguntas} Pergunta(s)\033[33m'.center(66) + '║')
print('╠════╦════════════════╦════════╦════════╦════════════════╣')
print('║ \033[36m#\033[33m  ║ \033[36mJogador\033[33m	      ║ \033[36mPts\033[33m    ║ \033[36mMult\033[33m   ║ \033[32mCertas \033[33m/\033[33m \033[31mErros\033[33m ║')
print('╠════╬════════════════╬════════╬════════╬════════════════╣')
for i, (nome, dados) in enumerate(jogadoresOrdenados, start=1):
    numJ = f' {i}'.ljust(4,' ')
    nomeJ = nome.ljust(15)
    pontosJ = f'{int(dados['pontuacao'])}'.rjust(6,' ')
    multJ = f'{dados['multiplicador']:.2f}'.rjust(6)
    acertosJ = f'{dados['acertos']} '.rjust(8)
    falhasJ = f' {dados['falhas']}'.ljust(7)
    print(f'║\033[36m{numJ}\033[33m║\033[36m{nomeJ} \033[33m║ \033[36m{pontosJ}\033[0m ║\033[36m{multJ}x \033[33m║\033[32m{acertosJ}\033[33m/\033[31m{falhasJ}\033[33m║')
    if i < nJogadores:
        print('╠════╬════════════════╬════════╬════════╬════════════════╣')
    else:
        print('╚════╩════════════════╩════════╩════════╩════════════════╝\033[0m')
