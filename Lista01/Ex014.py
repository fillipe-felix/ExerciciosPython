peso = float(input("Digite quantos quilos: "))
if(peso > 50):
    excesso = (peso - 50)
    multa = excesso * 4
print(f"João pegou {peso}Kg de peixe e ira pagar R${multa:.2f} de multa")