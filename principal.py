import json
import random
import os


# principal.py
class Pergunta:
    def __init__(self, id, pergunta, opcoes, resposta_correta):
        self.id = id
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.resposta_correta = resposta_correta

def carregar_perguntas(arquivo='perguntas.json'):
    if not os.path.exists(arquivo):
        return []
    with open(arquivo, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return [Pergunta(**p) for p in data['perguntas']]

def salvar_perguntas(perguntas, arquivo='perguntas.json'):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump({'perguntas': [p.__dict__ for p in perguntas]}, f, indent=4, ensure_ascii=False)

def adicionar_pergunta():
    perguntas = carregar_perguntas()
    nova_id = max([p.id for p in perguntas], default=0) + 1
    pergunta = input("Digite a pergunta: ")
    opcoes = []
    for i in range(4):
        opcoes.append(input(f"Opção {i+1}: "))
    resposta_correta = input("Resposta correta: ")

    nova = Pergunta(nova_id, pergunta, opcoes, resposta_correta)
    perguntas.append(nova)
    salvar_perguntas(perguntas)
    print("Pergunta adicionada com sucesso.")

def remover_pergunta():
    perguntas = carregar_perguntas()
    for p in perguntas:
        print(f"{p.id}: {p.pergunta}")
    id_remover = int(input("Digite o ID da pergunta a remover: "))
    perguntas = [p for p in perguntas if p.id != id_remover]
    salvar_perguntas(perguntas)
    print("Pergunta removida com sucesso.")

def jogar():
    perguntas = carregar_perguntas()
    if not perguntas:
        print("Não há perguntas registadas.")
        return

    random.shuffle(perguntas)
    score = 0

    for i, p in enumerate(perguntas[:5], 1):  # 5 perguntas por jogo
        print(f"\nPergunta {i}: {p.pergunta}")
        for idx, opcao in enumerate(p.opcoes):
            print(f"{idx + 1}. {opcao}")
        try:
            escolha = int(input("Escolha a opção correta (1-4): "))
            if p.opcoes[escolha - 1] == p.resposta_correta:
                print("✅ Correto!")
                score += 1
            else:
                print(f"❌ Errado! Resposta correta: {p.resposta_correta}")
        except:
            print("❌ Entrada inválida!")

    print(f"\n🎯 Resultado final: {score}/5")
    if score == 5:
        print("Excelente!")
    elif score >= 3:
        print("Muito bom!")
    else:
        print("Precisa estudar mais!")

def menu():
    while True:
        print("\n📚 Jogo de Conhecimentos")
        print("1. Jogar")
        print("2. Adicionar Pergunta")
        print("3. Remover Pergunta")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            jogar()
        elif escolha == '2':
            adicionar_pergunta()
        elif escolha == '3':
            remover_pergunta()
        elif escolha == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
