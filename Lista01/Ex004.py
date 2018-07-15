soma = 0
for c in range(1,5):
    nota = float(input(f"Digite a {c}º nota: "))
    soma = (soma + nota)
media = soma / c
print(f"A media foi de {media}")