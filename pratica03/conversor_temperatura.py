"""
4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

Celsius para Fahrenheit: °F = (°C * 9/5) + 32
Celsius para Kelvin: K = °C + 273.15
Fahrenheit para Celsius: °C = (°F - 32) * 5/9
Fahrenheit para Kelvin: K = (°F - 32) * 5/9 + 273.15
Kelvin para Celsius: °C = K - 273.15
Kelvin para Fahrenheit: °F = (K - 273.15) * 9/5 + 32

"""

temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a escala de origem (C, F ou K): ").upper()
destino = input("Digite a escala de destino (C, F ou K): ").upper()


if origem == destino:
    resultado = temperatura

elif origem == "C": # Se origem for Celsius, então converter para Fahrenheit ou Kelvin
    if destino == "F": 
        resultado = (temperatura * (9/5)) + 32 # Celsius para Fahrenheit
    else:
        resultado = temperatura + 273.15 # Celsius para Kelvin  

elif origem == "F": # Se origem for Fahrenheit, então converter para Celsius ou Kelvin
    if destino == "C":
        resultado = (temperatura - 32) * (5/9) # Fahrenheit para Celsius
    else:
        resultado = (temperatura - 32) * (5/9) + 273.15 # Fahrenheit para Kelvin

else: # Se origem for Kelvin, então converter para Celsius ou Fahrenheit
    if destino == "C":
        resultado = temperatura - 273.15 # Kelvin para Celsius
    else: 
        resultado = (temperatura - 273.15) * (9/5) + 32 # Kelvin para Fahrenheint   

print(f"\n{temperatura:.2f} {origem} é igual a {resultado:.2f} {destino}")    