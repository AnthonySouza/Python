'''

Algoritmo que recebe como entrada o primeiro nome do usuário e
responde se o nome dele é:

    pequeno <= 4 letras
    médio   >= 5 letras
    grande  >= 6 letras

'''

nome = input('Insire seu nome: ')
qnt_letras = len(nome)

try:

    if qnt_letras <= 4: # Pequeno
        print(f'Seu nome é pequeno! Ele tem {qnt_letras} letras!')

    elif qnt_letras < 6: # Médio
        print(f'Seu nome é médio! Ele tem {qnt_letras} letras!')

    elif qnt_letras > 6: # Grande
        print(f'Seu nome é grande! Ele tem {qnt_letras} letras!')

except:
    print('Ocorreu um erro, insira corretamente seu primeiro nome!')