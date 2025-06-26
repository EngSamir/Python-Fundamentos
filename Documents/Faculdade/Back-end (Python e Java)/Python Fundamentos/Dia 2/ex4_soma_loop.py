

soma = 0                                                                # Inicializa a variável que vai armazenar a soma


while True:                                                             # Laço infinito (será interrompido manualmente com break)
    numero = int(input("Digite um número (0 para parar): "))            # Pede número ao usuário
    if numero == 0:                                                     # Se o número for 0, sai do laço
        break

    soma += numero                                                      # Adiciona o número à soma


print(f"A soma dos números digitados é: {soma}")                        # Mostra o resultado final