def celsius_para_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

def fahrenheit_para_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9

def converter_temperatura():
    print("Escolha a opção de conversão:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        temp_celsius = float(input("Digite a temperatura em Celsius: "))
        temp_fahrenheit = celsius_para_fahrenheit(temp_celsius)
        print(f"A temperatura em Fahrenheit é: {temp_fahrenheit:.2f} °F")
    elif opcao == 2:
        temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        temp_celsius = fahrenheit_para_celsius(temp_fahrenheit)
        print(f"A temperatura em Celsius é: {temp_celsius:.2f} °C")
    else:
        print("Opção inválida. Por favor, escolha 1 ou 2.")

# Inicia a conversão de temperatura
converter_temperatura()
