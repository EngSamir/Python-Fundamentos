

numero = int(input("Digite um número para ver a tabuada: "))       # Pede um número ao usuário e converte para inteiro

print(f"\nTabuada do {numero}:\n")                                 # Cabeçalho formatado

for i in range(1, 11):                                             # Laço que vai de 1 a 10
    resultado = numero * i                                         # Multiplica o número pelo contador atual
    print(f"{numero} x {i} = {resultado}")                         # # Exibe a multiplicação formatada