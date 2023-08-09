def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None

    maior_palavra = menor_palavra = lista_palavras[0]

    for palavra in lista_palavras:
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra
        elif len(palavra) < len(menor_palavra):
            menor_palavra = palavra

    return maior_palavra, menor_palavra

# Exemplo de uso do programa
lista_palavras = input("Digite uma lista de palavras separadas por espaço: ").split()
maior, menor = encontrar_maior_menor_palavra(lista_palavras)

if maior is not None and menor is not None:
    print(f"Maior palavra: {maior}")
    print(f"Menor palavra: {menor}")
else:
    print("A lista de palavras está vazia.")
