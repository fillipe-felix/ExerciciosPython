"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = str(input("Digite uma letra para verificar se é vogal ou consoante: ")).upper()



if(letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U"):
    print(f"A letra {letra} é uma vogal")
else:
    print(f"A letra {letra} é uma consoante")