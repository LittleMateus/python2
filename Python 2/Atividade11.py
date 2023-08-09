import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação!")
    print("O computador escolheu um número entre 1 e 100. Tente adivinhar!")

    while True:
        try:
            palpite = int(input("Digite um número: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break
        elif palpite < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

# Inicia o jogo
jogo_adivinhacao()
