"""
Faça um Programa que leia três números e mostre o maior deles.
"""

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

maior = num1

if(num2 > maior and num2 > num3):
    maior = num2
elif(num3 > maior and num3 > num1):
    maior = num3

print(f"O numero maior é o {maior}")