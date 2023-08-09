def converter_para_maiusculas(lista_strings):
    palavras_maiusculas = [palavra.upper() for palavra in lista_strings]
    return palavras_maiusculas

# Exemplo de uso da função
lista_strings = ["o", "palmeiras", "é", "o melhor", "do mundo"]
palavras_maiusculas_resultado = converter_para_maiusculas(lista_strings)
print("Palavras em letras maiúsculas:", palavras_maiusculas_resultado)
