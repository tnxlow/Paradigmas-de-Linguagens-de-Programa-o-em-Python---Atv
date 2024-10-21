def calcular_media_quantidade():
    quantidade = int(input("Quantas notas você deseja calcular? "))
    notas = []
    
    for i in range(quantidade):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    print(f"Média Final: {media:.2f}")

calcular_media_quantidade()
