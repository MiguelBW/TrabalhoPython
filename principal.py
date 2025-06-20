import random
perguntasFile = r'dados\perguntas.txt'
respostasFile = r'dados\respostas.txt'

def quizz(nome, pontInicio, multInicio, nPerguntas, maiorNome):
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
        todaTabela = maiorNome + 41
        for x  in rdmPerguntas:
            print(f'\n\033[33m╔'+('═'*(todaTabela))+'╗')
            print(f'║\033[36mJOGADOR: \033[91m {nome}')
            esquerda = f'\033[33m║\033[36mPergunta: {i+1} de {nPerguntas}'
            direita = f'\033[36mMultiplicador: {multiplicador:.2f}x\033[0m'
            print(f'{esquerda}{direita.rjust(todaTabela - (5 + (2*len(str(nPerguntas))))," ")}',end='')
            print(f'\n\033[33m║\n║\033[0m{arrPerguntas[x-1]}',end='')

            y=0
            while y < len(arrRespostas):
                if x == int(arrRespostas[y]):
                    for j in range(1, 5):
                        linhaResposta = arrRespostas[y + j].rstrip()
                        print(f'\033[33m║\033[0m{opcoes[j-1]} - {linhaResposta[:-1]}',end='\n')
                        if linhaResposta.endswith('#'):
                            opcaoCorreta = opcoes[j-1]
                y+=5
            print('',end='\033[33m║')
            resposta = False
            while resposta == False:
                try:
                    inputUser = int(input())
                    if inputUser >= 1 and inputUser <= 4:
                        if str(inputUser).lower() == str(opcaoCorreta).lower():
                            
                            acertos += 1
                            pontuacao += (valorPergunta * multiplicador)
                            multiplicador += multAcerto
                            resposta = True
                            if (valorPergunta * multiplicador) > 0:
                                print(f'\033[33m║\033[92mCORRETO + {(valorPergunta * multiplicador):.0f} 🗿')
                            else:
                                print(f'\033[33m║\033[92mCORRETO\033[91m {(valorPergunta * multiplicador):.0f} 🤣👌')
                        else:
                            print(f'\033[33m║\033[91mINCORRETO 😫 {multFalha}x\n\033[33m║\033[92mresposta correta: {opcaoCorreta}')
                            falhas += 1
                            multiplicador += multFalha
                            resposta = True
                    else:
                        print(f'\033[33m║\033[91mInsira uma resposta válida 1 - 4',end='\n\033[33m║')
                except ValueError:
                    print(f'\033[33m║\033[91mInsira uma resposta válida 1 - 4',end='\n\033[33m║')
            print(f'\033[33m╠'+('═'*(todaTabela))+'╣')
            i += 1
            if multiplicador >= 0:
                print(f'\033[33m║\033[36mMultiplicador: \033[92m{multiplicador:.2f}x  ',end='')
            else:
                print(f'\033[33m║\033[36mMultiplicador: \033[91m{multiplicador:.2f}x  ',end='')
            if pontuacao >= 0:
                print(f'\033[36mPONTUAÇÃO: \033[92m{pontuacao:.1f}',end='\n')
            else:
                print(f'\033[36mPONTUAÇÃO: \033[91m{pontuacao:.1f}',end='\n')
            print(f'\033[33m║\033[36mDe {nPerguntas} Pergunta(s)\033[92m   Acertou: {acertos}\033[91m   Falhou: {falhas}\033[0m',end='\n')
            print(f'\033[33m╚'+('═'*(todaTabela))+'╝')

        return(pontuacao, multiplicador,acertos,falhas)
    except FileNotFoundError as e:
        print(f'erro: {e}')
        return(pontFinal,multFinal,acertos,falhas)

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
                        print(f'\033[91mA sair...')
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
                print(f'\033[91mA sair...')
                quit()
            else:
                return nJogadores
        except ValueError:
            print(f'\033[91mPor Favor, Insira um número...\033[0m')

def mostrarResultados():
    jogadoresOrdenados = sorted(jogadores.items(), key=lambda item: item[1]['pontuacao'], reverse=True)
    print('\n\033[33m╔'+('═'*maiorNome)+'═════════════════════════════════════════╗')
    print('║' + f'\033[95mRANKING FINAL - {nPerguntas} Pergunta(s)\033[33m'.center(51 + maiorNome) + '║')
    print('╠════╦═'+('═'*maiorNome)+'╦════════╦════════╦════════════════╣')
    print('║ \033[36m#\033[33m  ║ \033[36m'+'Jogador'.ljust(maiorNome)+'\033[33m║ \033[36mPts\033[33m    ║ \033[36mMult\033[33m   ║ \033[32mCertas \033[33m/\033[33m \033[31mErros\033[33m ║')
    print('╠════╬═'+('═'*maiorNome)+'╬════════╬════════╬════════════════╣')
    for i, (nome, dados) in enumerate(jogadoresOrdenados, start=1):
        numJ = f' {i}'.ljust(4)
        nomeJ = nome.ljust(maiorNome-1,' ')
        pontosJ = f"{int(dados['pontuacao'])}".rjust(6)
        multJ = f"{dados['multiplicador']:.2f}".rjust(6)
        acertosJ = f"{dados['acertos']} ".rjust(8)
        falhasJ = f" {dados['falhas']}".ljust(7)
        print(f'║\033[36m{numJ}\033[33m║ \033[36m{nomeJ} \033[33m║ \033[36m{pontosJ}\033[33m ║\033[36m{multJ}x \033[33m║\033[32m{acertosJ}\033[33m/\033[31m{falhasJ}\033[33m║')
        if i < nJogadores:
            print('╠════╬═'+('═'*maiorNome)+'╬════════╬════════╬════════════════╣')
        else:
            print('╚════╩═'+('═'*maiorNome)+'╩════════╩════════╩════════════════╝\033[0m')
            
def jogar():
    print(f'\n\33[0mO multiplicador começa em \033[36m1.00x\033[0m após cada acerto aumenta \033[92m+0.10\033[0m a cada falha diminui \033[91m-0.20\033[0m\nO Jogador com maior pontuação vence, \033[92mBoa Sorte!\033[0m')
    global maiorNome,jogadores,nPerguntas,nJogadores,pontFinal,multFinal
    jogadores = {}
    nPerguntas = qtdPerguntas()
    nJogadores = qtdJogadores()

    for x in range(nJogadores):
        nome = input(f'\033[36mPlayer \033[91m{x+1}\033[36m Insira seu username: \033[0m')
        jogadores[nome] = {'pontuacao': 0.0, 'multiplicador': 1.0, 'acertos': 0, 'falhas': 0}
    maiorNome = 15
    for nome in jogadores:
        pont, mult = jogadores[nome]['pontuacao'], jogadores[nome]['multiplicador']
        pontFinal, multFinal, acertos, falhas = quizz(nome, pont, mult, nPerguntas, maiorNome)
        jogadores[nome]['pontuacao'] = pontFinal
        jogadores[nome]['multiplicador'] = multFinal
        jogadores[nome]['acertos'] = acertos
        jogadores[nome]['falhas'] = falhas
        if len(nome) > maiorNome:
            maiorNome = len(nome) + 1

    mostrarResultados()
    
def lerPerguntas():
    with open(perguntasFile, 'r', encoding='utf-8') as perguntasF:
        return(perguntasF.readlines())
    
def lerRespostas():
    with open(respostasFile, 'r', encoding='utf-8') as respostasF:
        return(respostasF.readlines())



def listarPerguntas():
        arrPerguntas = lerPerguntas()
        arrRespostas = lerRespostas()
        if len(arrPerguntas) <= 0:
            print(f'Não existem perguntas.')
            return
        x = 0
        y = 0
        found = False
        while x < len(arrPerguntas):
            print('\033[33m'+'═'*50+'\033[0m')
            print(f'\033[95mPergunta {x+1} \033[0m-\033[36m {arrPerguntas[x].strip()}')
            while not found:
                if int(x+1) != int(arrRespostas[y]):
                    y += 5
                else:
                    found = True
                    for z in range(1,5):
                        resposta = arrRespostas[y+z].strip()
                        if resposta.endswith('#'):
                            print(f'\033[32mOpção {z} - {resposta[:-1]}')
                        else:
                            print(f'\033[31mOpção {z} - {resposta[:-1]}')
                        
            print('\033[33m'+'═'*50+'\033[0m')
            print()
            found = False
            y = 0
            x += 1
def adicionarPergunta():
    arrPerguntas = lerPerguntas()
    arrRespostas = lerRespostas()
    numPerguntas = len(arrPerguntas)
    
    pergunta = input('\033[36mInsira a pergunta: \033[0m')
    if numPerguntas < 1:
        arrPerguntas.append(pergunta)
        arrRespostas.append(f'{len(arrPerguntas)}')
    else:
        arrPerguntas.append('\n' + pergunta)
        arrRespostas.append(f'\n{len(arrPerguntas)}')
    
    print('\033[33mInsira 4 opções de resposta: ')
    
    respostas = []
    usadas = set()

    for i in range(4):
        while True:
            r = input(f'\033[36mDigite a resposta \033[33m{i+1}\033[36m:\033[0m ').strip().rstrip('.#')
            if r in usadas:
                print('\033[91mResposta repetida. Digite outra.\033[0m')
            else:
                usadas.add(r)
                respostas.append(r)
                break

    correta = int(input('\033[92mQual é a resposta correta? (1 a 4): ')) - 1

    for i in range(4):
        if i == correta:
            respostas[i] += '#'
            arrRespostas.append('\n' + respostas[i])
        else:
            respostas[i] += '.'
            arrRespostas.append('\n' + respostas[i])

    arrPerguntas = [linha.strip() + '\n' for linha in arrPerguntas]
    arrRespostas = [linha.strip() + '\n' for linha in arrRespostas]
    with open(perguntasFile, 'w', encoding='utf-8') as perguntasF:
        perguntasF.writelines(arrPerguntas)

    with open(respostasFile, 'w', encoding='utf-8') as respostasF:
        respostasF.writelines(arrRespostas)
        
def removerPergunta():
    while True:
        try:
            arrPerguntas = lerPerguntas()
            arrRespostas = lerRespostas()
            numPerguntas = len(arrPerguntas)
            if  numPerguntas <= 0:
                print('\033[33m╔' + '═' * 23 + '╗')
                print(f'║\033[91m Não existem perguntas \033[33m║')
                print('╚' + '═' * 23 + '╝\033[33m')
            
                return
            elif numPerguntas == 1:
                print('\033[33m╔' + '═' * 20 + '╗')
                print(f'║\033[92m Existe 1 pergunta  \033[33m║')
                print('╚' + '═' * 20 + '╝\033[33m')
            else:
                print('\033[33m╔' + '═' * 24 + '╗')
                print(f'║\033[92m  Existem {numPerguntas} perguntas  \033[33m║')
                print('╚' + '═' * 24 + '╝\033[33m')
                
            num = int(input('Insira o número da pergunta que deseja remover:\033[0m '))
            if num == 0:
                print(f'\033[91mA voltar...')
                return
            elif num < 1 or num > numPerguntas:
                print(f'\033[91mPor favor insira um número válido!')
            else:
                perguntaRemovida = arrPerguntas.pop(num - 1)

                y = 0
                found = False
                while y < len(arrRespostas):
                    if arrRespostas[y].strip() == str(num):
                        found = True
                        for _ in range(5):
                            arrRespostas.pop(y)
                        break
                    y += 5

                if found:
                    y = 0
                    nPergunta = 1
                    while y < len(arrRespostas):
                        arrRespostas[y] = f'{nPergunta}\n'
                        nPergunta += 1
                        y += 5
                    try:
                        arrPerguntas = [linha.strip() + '\n' for linha in arrPerguntas]
                        with open(perguntasFile, 'w', encoding='utf-8') as perguntasF:
                            perguntasF.writelines(arrPerguntas)
                        with open(respostasFile, 'w', encoding='utf-8') as respostasF:
                            respostasF.writelines(arrRespostas)
                        print(f'\033[36mPergunta removida:\033[91m {perguntaRemovida}')
                        
                    except FileNotFoundError as e:
                        print(f'erro: {e}')
                        quit()
                        
        except ValueError:
            print(f'\033[91mPor favor insira um número válido!')
def menu():
    while True:
        print('\033[33m╔' + '═' * 20 + '╗')
        print('║\033[95m Perguntas\033[33m          ║')
        print('║   \033[36m1. Listar\033[33m        ║')
        print('║   \033[36m2. Remover\033[33m       ║')
        print('║   \033[36m3. Adicionar\033[33m     ║')
        print('║ \033[95mJogar\033[33m              ║')
        print('║   \033[36m4. Go!\033[33m           ║')
        print('║   \033[36m0. Sair\033[33m          ║')
        print('╠' + '═' * 20 + '╣\033[33m')
        opcao = input('║ Escolha: ')
        print('╚' + '═' * 20 + '╝\033[33m')

        match opcao:
            case '1':
                listarPerguntas()
            case '2':
                removerPergunta()
            case '3':
                adicionarPergunta()
            case '4':
                jogar()
            case '0':
                print(f'\033[91m A sair...')
                break
            case _:
                print('Opção inválida.')

menu()