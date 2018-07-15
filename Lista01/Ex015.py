"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para
o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo: 
"""
salHora = float(input("Digite o salario por hora: "))
horasMes = float(input("Digite quantas horas trabalhou no mes: "))

salBruto = salHora * horasMes
IR = salBruto * 0.11
INSS = salBruto * 0.08
sindicato = salBruto * 0.05
salLiquido = salBruto - IR - INSS - sindicato

print(f"\n+Salario Bruto R${salBruto:.2f}\n-IR = {IR:.2f}\n-INSS = {INSS:.2f}\n-Sindicato = {sindicato:.2f}\nSalario Liquido = {salLiquido:.2f}\n")