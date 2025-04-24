votos_candidatos = [0, 0, 0, 0]  
votos_nulos = 0
votos_brancos = 0
total_votos = 0

numero_eleitores = 10

print("Digite o código do voto para cada eleitor:")
print("1 a 4: Candidatos | 5: Nulo | 6: Branco")

for i in range(numero_eleitores):
    voto = int(input(f"Voto do eleitor {i+1}: "))
    total_votos += 1

    if voto in [1, 2, 3, 4]:
        votos_candidatos[voto - 1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_brancos += 1
    else:
        print("Voto inválido! Ignorado.")
        total_votos -= 1  

# Cálculos
votos_validos = sum(votos_candidatos)

print("\nResultado da votação:")
for i, votos in enumerate(votos_candidatos):
    percentual = (votos / votos_validos * 100) if votos_validos else 0
    print(f"Candidato {i+1}: {votos} votos ({percentual:.2f}%)")

print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_brancos}")

percentual_nulos = (votos_nulos / total_votos * 100) if total_votos else 0
percentual_brancos = (votos_brancos / total_votos * 100) if total_votos else 0

print(f"Percentual de votos nulos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco: {percentual_brancos:.2f}%")
