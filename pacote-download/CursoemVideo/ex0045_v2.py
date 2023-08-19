import random

def escolha_jogador():
    print("Escolha sua jogada:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    escolha = int(input("Digite o número da sua escolha: "))
    if escolha not in [1, 2, 3]:
        print("Escolha inválida! Tente novamente.")
        return escolha_jogador()
    return escolha

def escolha_computador():
    return random.randint(1, 3)

def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        return "Jogador"
    else:
        return "Computador"

def imprimir_resultado(vencedor, jogador, computador):
    print(f"Você escolheu: {jogadas[jogador]}")
    print(f"O computador escolheu: {jogadas[computador]}")
    print(f"Resultado: {vencedor} vence!")

jogadas = {1: "🪨 Pedra", 2: "📄 Papel", 3: "✂️ Tesoura"}

while True:
    jogador = escolha_jogador()
    computador = escolha_computador()
    vencedor = determinar_vencedor(jogador, computador)
    imprimir_resultado(vencedor, jogador, computador)
    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() != "s":
        break