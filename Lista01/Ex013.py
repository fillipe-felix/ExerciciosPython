altura = float(input("Digite a sua altura: "))
sexo = str(input("Digite o seu sexo 'F'/'M': ")).upper()
if(sexo == "M"):
    pesoIdeal = (72.7 * altura) - 58
    print(f"Seu peso ideal é de {pesoIdeal:.2f}")
if(sexo == "F"):
    pesoIdeal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é de {pesoIdeal:.2f}")