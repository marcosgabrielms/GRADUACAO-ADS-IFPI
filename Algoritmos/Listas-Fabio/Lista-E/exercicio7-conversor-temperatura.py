# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. O programa deve:
# Validar temperaturas mínimas (Kelvin não pode ser < 0, Celsius não pode ser < -273.15)
# Permitir que o usuário escolha a unidade de origem e destino
# Fornecer o resultado com 2 casas decimais

from io_utils import escolher_unidade, ler_temperatura, exibir_resultado

def validar_celsius(temp):
    return temp >= -273.15

def validar_Fahrenheit(temp): 
    return temp >= -459.67

def validar_kelvin(temp):
    return temp >= 0

def celsius_para_Fahrenheit(temp):
    return (temp * 9/5) + 32

def celsius_para_kelvin(temp):
    return temp + 273.15

def Fahrenheit_para_celsius(temp):
    return (temp - 32) * 5/9

def Fahrenheit_para_kelvin(temp):
    return (temp - 32) * 5/9 + 273.15

def kelvin_para_celsius(temp):
    return temp - 273.15

def kelvin_para_Fahrenheit(temp):
    return (temp - 273.15) * 9/5 + 32

def converter_temperatura(origem, destino, temp):
    if origem == destino:
        return temp
    
    if origem == "Celsius":
        if destino == "Fahrenheit":
            return celsius_para_Fahrenheit(temp)
        elif destino == "Kelvin":
            return celsius_para_kelvin(temp)
    
    elif origem == "Fahrenheit":
        if destino == "Celsius":
            return Fahrenheit_para_celsius(temp)
        elif destino == "Kelvin":
            return Fahrenheit_para_kelvin(temp)
        
        elif origem == "Kelvin":
            if destino == "Celsius":
                return kelvin_para_celsius(temp)
            elif destino == "Fahrenheit":
                return kelvin_para_Fahrenheit(temp)

def validar_temperatura(unidade, temp):
    if unidade == "Celsius":
        return validar_celsius(temp)  
    elif unidade == "Fahrenheit":
        return validar_Fahrenheit(temp)
    elif unidade == "Kelvin":
        return validar_kelvin(temp)

def main():
    print("\nConversor de tempertatura")     

    origem = escolher_unidade()
    destino = escolher_unidade()

    temp = ler_temperatura(origem)

    if not validar_temperatura(origem, temp):
        print("Temperatura inválida para " + origem + "!")
        return main()

    resultado = converter_temperatura(origem, destino, temp)
    exibir_resultado(resultado, destino)

if __name__ == "__main__":
    main()        