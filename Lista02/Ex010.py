"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino 
ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou 
"Boa Noite!" ou "Valor Inválido!", conforme o caso
"""

periodo = str(input("Digite M-matutino ou V-Vespertino ou N- Noturno: ")).upper()

if(periodo == "M"):
    print("Bom dia!")
elif(periodo == "V"):
    print("Boa tarde!")
elif(periodo == "N"):
    print("Boa noite!")
else:
    print("Valor invalido!")