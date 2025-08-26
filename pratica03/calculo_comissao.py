"""
6- Calculadora de Comissão

Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
"""

nome_vendedor = input("Insira o nome do vendedor: ")
salario_fixo = float(input("Insira o salário fixo (Ex: 2500.00): "))
total_vendas = float(input("Insira o total de vendas (Ex: 50000.00): "))


comissao = total_vendas * 0.15

salario_total = salario_fixo + comissao


print(f"""
Nome do funcionário: {nome_vendedor}
Salário total: R$ {salario_total:.2f}
""")