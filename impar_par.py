'''

Faça um programa que leia um número inteiro e diga se ele é par ou ímpar.

'''

# Entrada
numero = input('Digite um número: ')

# Converte str para int
try:
    numero = int(numero)
except:
    numero = input('Digite um número válido: ')

# Faz o processamento
if (numero % 2) == 0: # Caso o resto da divisão seja igual a 0, é par
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')