jogadores = [
    {"nome": "João", "pontos": 100000, "multiplicador": 1000, "certas": 18, "erradas": 2},
    {"nome": "Ana", "pontos": 1650, "multiplicador": 1.5, "certas": 15, "erradas": 5},
    {"nome": "Miguel", "pontos": 900, "multiplicador": 1, "certas": 9, "erradas": 11},
    {"nome": "Carla", "pontos": 2200, "multiplicador": 2, "certas": 22, "erradas": 0}
]
jogadores_ordenados = sorted(jogadores, key=lambda x: x['pontos'], reverse=True)

print("╔════════════════════════════════════════════════════════╗")
print("║                      RANKING FINAL                     ║")
print("╠════╦════════════════╦════════╦════════╦════════════════╣")
print("║ #  ║ Jogador        ║ Pts    ║ Mult   ║ Certas / Erros ║")
print("╠════╬════════════════╬════════╬════════╬════════════════╣")
for i, jogador in enumerate(jogadores_ordenados, 1):
        nome = jogador['nome'].ljust(14)
        pontos = str(jogador['pontos']).ljust(6)
        mult = f"x{jogador['multiplicador']}".ljust(6)
        certas_erradas = f"{jogador['certas']}\t/ {jogador['erradas']}\t"
        print(f"║ {str(i).ljust(2)} ║ {nome} ║ {pontos} ║ {mult} ║ {certas_erradas} ║")

print("╚════╩════════════════╩════════╩════════╩════════════════╝")


# Exemplo de jogadores
jogadores = [
    {"nome": "João", "pontos": 1800, "multiplicador": 2, "certas": 18, "erradas": 2},
    {"nome": "Ana", "pontos": 1650, "multiplicador": 1.5, "certas": 15, "erradas": 5},
    {"nome": "Miguel", "pontos": 900, "multiplicador": 1, "certas": 9, "erradas": 11},
    {"nome": "Carla", "pontos": 2200, "multiplicador": 2, "certas": 22, "erradas": 0}
]