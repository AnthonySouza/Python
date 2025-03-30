'''

Iterando strings com while...
    input = recebe um nome
    verifica qtd de caracteres
    adiciona * após cada caractere
    ex: input Gabriel => *G*a*b*r*i*e*l*

'''

nome = input('Insira seu nome: ')
nome_iterado = ''

if nome: # Se tiver algo
    qnt_caractere = len(nome)
    index = 0
    
    while index < qnt_caractere: # Enquanto o index for < ou = que a quantidade de caracteres...
        caracter_atual = nome[index] # Seleciona o carcater atual do laço...
        nome_iterado += f'*{caracter_atual}' # Adiciona * seguido do caracter atual na variável nome_iterado
        index += 1 # Atualiza o índice

        if index == qnt_caractere: # Caso o laço tenha percorrido todas as letras, adiciona o último * e sai do loop...
            nome_iterado = nome_iterado + f'*'
            break

else: # Se estiver vazio, lança o erro
    print('Você precisa inserir algum nome!')

print(f'Resultado: {nome_iterado}') # Returna o resultado