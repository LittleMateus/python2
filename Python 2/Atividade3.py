def imprimir_numeros_naturais(n):
    if n < 0:
        print("Por favor, digite um número inteiro positivo.")
        return

    for i in range(n + 1):
        print(i)

# Lê um número inteiro positivo do usuário
numero = int(input("Digite um número inteiro positivo: "))

# Chama a função para imprimir os números naturais
imprimir_numeros_naturais(numero)