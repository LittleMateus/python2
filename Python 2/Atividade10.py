def encontrar_maior_menor_numero(sequencia):
    if not sequencia:
        return None, None

    maior_numero = menor_numero = sequencia[0]

    for numero in sequencia:
        if numero > maior_numero:
            maior_numero = numero
        elif numero < menor_numero:
            menor_numero = numero

    return maior_numero, menor_numero

# Leitura da sequência de números
entrada = input("Digite uma sequência de números separados por espaço: ")
sequencia_numeros = [int(numero) for numero in entrada.split()]

# Encontra o maior e o menor número da sequência
maior, menor = encontrar_maior_menor_numero(sequencia_numeros)

if maior is not None and menor is not None:
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
else:
    print("A sequência está vazia.")
