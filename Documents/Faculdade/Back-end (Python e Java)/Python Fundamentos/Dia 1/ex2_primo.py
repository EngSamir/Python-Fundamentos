

def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):      # Testa até a raiz quadrada de n
        if n % i == 0:                       # Se dividir por algum número, não é primo
            return False
    return True 

# Teste
print(eh_primo(7))   # True 
print(eh_primo(10))  # False