"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina 
ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if(media >= 9):
    conceito = "A"
elif(media >= 7.5 and media < 9):
    conceito = "B"
elif(media >= 6 and media < 7.5):
    conceito = "C"
elif(media >= 4 and media < 6):
    conceito = "D"

if(conceito == "A" or "B" or "c"):
    resultado = "Aprovado"
elif(conceito == "D" or "E"):
    resultado = "Reprovado"

print(f"Primeira Nota {nota1}")
print(f"Segunda Nota {nota2}")
print(f"Media do aluno {media:.2f}")
print(f"Nota conceito do aluno \"{conceito}\"")
print(f"Resultado final {resultado}")