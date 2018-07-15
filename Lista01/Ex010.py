"""Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit."""

celsius = float(input("Digite quantos graus Celsius: "))
faren = 1.8 * celsius + 32
print(f"{celsius}ºC é igual a {faren:.2f}ºF")