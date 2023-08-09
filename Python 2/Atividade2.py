def calcular_media(lista):
    if not lista:
        return 0  
    soma = sum(lista)
    media = soma / len(lista)
    return media

lista_numeros = [10, 20, 30, 40, 50]
media_resultado = calcular_media(lista_numeros)
print("A média dos números é:", media_resultado)