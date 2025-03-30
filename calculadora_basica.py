'''

Calculadora básica em python
    entrada:
        numero
        operação [+], [-], [*] e [/]

'''

numero_1 = ''
numero_2 = ''
operador = ''
nome_operador = ''
resultado = 0

numero_1 = input('Insira o primeiro número: ')

# Verifica se é número válido
if numero_1.isdigit():
    # Converte para int
    numero_1 = int(numero_1)

    # Recebe o operador e trata a entrada
    operador = input('Insira um operador entre [+], [-], [*] e [/]: ')
    if operador == '+':
        nome_operador = 'somar'

    elif operador == '-':
        nome_operador = 'subtrair'

    elif operador == '*':
        nome_operador = 'multiplicar'

    elif operador == '/':
        nome_operador = 'dividir'        

    else:
        print('Insira um operador válido! [+], [-], [*] e [/].')

    # Recebe o segundo número para operação matemática
    numero_2 = input(f'Insira o segundo número para {nome_operador}: ')

    # Verifica se é número válido
    if numero_2.isdigit():
        # Converte em int
        numero_2 = int(numero_2)

    else:
        print('Você precisa digitar um número válido!')

else:
    print('Você precisa digitar um número válido!')

# Calcula a operação
if operador == '+':
    resultado = numero_1 + numero_2 

if operador == '-':
    resultado = numero_1 - numero_2

if operador == '*':
    resultado = numero_1 * numero_2

if operador == '/':
    resultado = numero_1 // numero_2

# Mostra o resultado no console
print(f'O resultado da {nome_operador} é: {resultado}')