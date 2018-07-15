"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

m2 = float(input("Digite a area a ser pintada em metros Quadrados: "))

litros = m2 / 3
precoLitro = 80
capacidadeLitro = 18
latas = litros / capacidadeLitro
total = latas * precoLitro

print(f"Voce ira utilizar {latas:.2f} latas de tinta")
print(f"O preço total das latas é de R${total:.2f}")