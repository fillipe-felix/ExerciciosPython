"""
Faça um Programa que peça a temperatura em graus Farenheit,
 transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9). 
"""

faren = float(input("Digite quantos graus Farenheit: "))
celsius = (5 * (faren - 32) / 9)
print(f"{faren}ºF é igual a {celsius:.2f}ºC")