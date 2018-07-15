"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if(num1 > num2 ):
    maior = num1
else: 
    maior = num2

print(f"O numero maior entre os dois é {maior:.2f}")