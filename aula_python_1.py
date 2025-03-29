'''

Aula 1 - Python Básico
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade

Se nome e idade forem digitados:

exibe:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome tem espaços em branco
    Seu nome tem {n} letras
    A primeira letra do seu nome é {primeira letra}
    A última letra do seu nome é {última letra}
    Você tem {n} anos!

Se nada for digitado:
    exibe: "Você não digitou nada!"

'''

print('Olá, digite seus dados abaixo:')

nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')

# Verifica se o usuário digitou a entrada idade corretamente "int"
if idade.isnumeric():
    idade = int(idade)  # Converte a idade para int
else: #Se não
    print('Idade inválida! tente novamente')
    idade = input('Qual sua idade? ')

# Verifica se a idade é válida
if (idade == 0 or idade >= 120): 
    print('Idade inválida! tente novamente')
    idade = input('Qual sua idade? ')
elif (idade == ''):
    print('Idade inválida! tente novamente')


if nome and idade:
    print(f'Seu nome é {nome}\n')
    print(f'Seu nome invertido é {nome[::-1]}\n')
    
    if(' ' in nome):
        print('Seu nome contem espaços em branco\n')
    else:
        print('Seu nome não contem espaços em branco\n')
    
    print(f'Seu nome tem {len(nome)} letras\n')
    print(f'A primeira letra do seu nome é {nome[0]}\n')
    print(f'A última letra do seu nome é {nome[-1]}\n')
    print(f'Você tem {idade} anos!\n')
else:
    print('Você não digitou nada!\n')

print('Fim do programa\n')