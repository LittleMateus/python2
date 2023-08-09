def calcular_mediana(lista_numeros):
    lista_ordenada = sorted(lista_numeros)
    tamanho = len(lista_ordenada)

    if tamanho % 2 == 0:
        indice_meio = tamanho // 2
        mediana = (lista_ordenada[indice_meio - 1] + lista_ordenada[indice_meio]) / 2
    else:
        indice_meio = tamanho // 2
        mediana = lista_ordenada[indice_meio]

    return mediana

# Exemplo de uso da função
lista_numeros = [10, 5, 2, 8, 15, 7]
mediana_resultado = calcular_mediana(lista_numeros)
print("Mediana dos valores:", mediana_resultado)
