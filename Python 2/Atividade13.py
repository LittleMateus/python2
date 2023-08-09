def contar_ocorrencias_palavras(texto):
    palavras = texto.split()
    contador = {}

    for palavra in palavras:
        palavra = palavra.lower()  # Converte para letras minúsculas 
        palavra = palavra.strip(",.;!?()[]{}\"'")  # Remove pontuações ao redor das palavras
        if palavra in contador:
            contador[palavra] += 1
        else:
            contador[palavra] = 1

    return contador

# Leitura do texto do usuário
texto = input("Digite um texto: ")

# Contagem das ocorrências das palavras
resultado_contagem = contar_ocorrencias_palavras(texto)

# Imprime o resultado
print("Quantidade de ocorrências de cada palavra:")
for palavra, ocorrencias in resultado_contagem.items():
    print(f"{palavra}: {ocorrencias}")
