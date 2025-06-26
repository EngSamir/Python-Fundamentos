

def potencia(base, expoente):                                 # Essa linha define uma função chamada potencia que recebe dois parâmetros: base e expoente.
    return base ** expoente                                   # O operador ** em Python serve para calcular potências.

base = int(input("Digite o número base: "))
expoente = int(input("Digite o expoente: "))


resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é {resultado}")           # O f"" é uma f-string (string formatada), que permite inserir variáveis diretamente no texto.