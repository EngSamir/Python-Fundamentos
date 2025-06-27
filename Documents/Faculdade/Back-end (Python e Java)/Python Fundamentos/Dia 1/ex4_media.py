

def media(notas):
    total = sum(notas)                  # Soma todas as notas
    return total / len(notas)           # Divide pelo número de notas

# Teste
notas = [7.5, 8.0, 6.5]
print("Media:", media(notas))           # Deve imprimir algo como 7.33