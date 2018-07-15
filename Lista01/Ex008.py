"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
 """

salHora = float(input("Digite o salario por hora: "))
totHoras = float(input("Digite quantas horas trabalhou no mes: "))
salario = salHora * totHoras
print(f"O seu salario do mes foi de R${salario:.2f}")