def calcular_media():
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    print(f"Média Final: {media:.2f}")
    
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

calcular_media()