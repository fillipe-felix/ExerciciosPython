"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""

num = float(input("Digite um numero qualquer: "))

if(num > 0):
    print(f"O numero {num} é positivo")
elif(num < 0):
    print(f"O numero {num} é negativo")
else:
    print(f"O numero {num} é nulo ou 0")