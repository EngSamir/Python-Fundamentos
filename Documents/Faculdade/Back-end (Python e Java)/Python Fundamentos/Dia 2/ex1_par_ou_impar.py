

numero = int(input("Digite um número inteiro: "))     # input() mostra a mensagem e aguarda o usuário digitar algo.
if numero % 2 == 0:                                   # int() converte o valor digitado (que vem como texto) para um número inteiro.
    print("O número é par.")                          # numero % 2 calcula o resto da divisão por 2.
else:                                                 # O if é a estrutura condicional que executa um bloco de código somente se essa condição for verdadeira e O else é usado para definir o que acontece quando a condição do if é falsa.
    print("ímpar")                                    # O print() exibe a mensagem "O número é par." no terminal