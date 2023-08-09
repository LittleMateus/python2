def calcular_fatorial(numero):
    if numero < 0:
        return None  
    elif numero == 0:
        return 1  
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial


numero = int(input("Digite um número inteiro não negativo: "))
resultado_fatorial = calcular_fatorial(numero)

if resultado_fatorial is not None:
    print(f"O fatorial de {numero} é: {resultado_fatorial}")
else:
    print("O fatorial não é definido para números negativos.")
