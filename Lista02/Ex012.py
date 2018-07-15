"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3%
para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, dispostas conforme
o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

salHora = float(input("Digite quanto ganha por hora: "))
totHora = float(input("Digite o total de horas trabalhadas no mes: "))

salarioBruto = salHora * totHora
FGTS = salarioBruto * 0.11
sindicato = salarioBruto * 0.03

if(salarioBruto <= 900):
    INSS = salarioBruto * 0.10
    IR = salarioBruto * 0
    descontos = sindicato + IR + INSS
    salarioLiquido = salarioBruto - descontos
elif(salarioBruto <= 1500):
    INSS = salarioBruto * 0.10
    IR = salarioBruto * 0.05
    descontos = sindicato + IR + INSS
    salarioLiquido = salarioBruto - descontos
elif(salarioBruto <= 2500):
    INSS = salarioBruto * 0.10
    IR = salarioBruto * 0.10
    descontos = sindicato + IR + INSS
    salarioLiquido = salarioBruto - descontos
else:
    INSS = salarioBruto * 0.10
    IR = salarioBruto * 0.20
    descontos = sindicato + IR + INSS
    salarioLiquido = salarioBruto - descontos

print(f"Salario Bruto :R${salarioBruto:.2f}")
print(f"(-) IR R${IR:.2f}")
print(f"(-) INSS R${INSS:.2f}")
print(f"FGTS R${FGTS:.2f}")
print(f"Total de Descontos {descontos:.2f}")
print(f"Salario Liquido {salarioLiquido:.2f}")
