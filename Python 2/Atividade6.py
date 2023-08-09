import random

def lancamento_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    return dado1, dado2

# Função para calcular a soma dos valores dos dados
def calcular_soma_dados(dado1, dado2):
    return dado1 + dado2

# Simulação do lançamento dos dados
dado1, dado2 = lancamento_dados()

# Cálculo da soma dos valores dos dados
soma = calcular_soma_dados(dado1, dado2)

# Imprime os resultados
print(f"Resultado do lançamento: Dado 1 = {dado1}, Dado 2 = {dado2}, Soma = {soma}")
