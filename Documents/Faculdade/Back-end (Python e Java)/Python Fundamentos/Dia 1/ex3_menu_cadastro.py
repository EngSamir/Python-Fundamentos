

usuarios = []                                       # Lista Vazia para guardar nomes

while True:
    nome = input("Digite um nome (ou 'sair'): ")    # Pede um nome oa usuário
    if nome.lower() == "sair":                      # Se digitar 'sair', para o loop
        break
    usuarios.append(nome)                           # Adiciona o nome à lista


print("Usuários cadastrados:", usuarios)            # Mostra os nomes cadastrados