
"""
Calculadora de Consumo de Combustível
 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
Distância percorrida: 300 km
Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""
# Dados da viagem
distancia = 300
combustivel = 25

# Cálculo do Consumo
consumo = distancia / combustivel

# Exibição dos resultados
print(f"""
Distância Percorrida: {distancia} km
Combustível Gasto: {combustivel} l
Consumo Médio: {round(consumo, 2)} km/l
""")
