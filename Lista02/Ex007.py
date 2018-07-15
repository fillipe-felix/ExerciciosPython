"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))

menor = num1

if(num2 < menor and num2 < num3):
    menor = num2
elif(num3 < menor and num3 < num1):
    menor = num3

print(f"O numero menor é o {menor}")