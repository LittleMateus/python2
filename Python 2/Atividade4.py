def eh_palindromo(palavra):
    
    palavra = palavra.replace(" ", "").lower()

    
    if palavra == palavra[::-1]:
        return True
    else:
        return False


palavra_teste = "mateus"
resultado = eh_palindromo(palavra_teste)

if resultado:
    print(f"{palavra_teste} é um palíndromo!")
else:
    print(f"{palavra_teste} não é um palíndromo.")
