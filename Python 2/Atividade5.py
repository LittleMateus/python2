def filtrar_numeros_pares(lista):
    numeros_pares = [numero for numero in lista if numero % 2 == 0]
    return numeros_pares


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares_resultado = filtrar_numeros_pares(lista_numeros)
print("Números pares:", numeros_pares_resultado)
