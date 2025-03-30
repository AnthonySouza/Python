'''

Algoritmo que recebe a hora do dia e responde com uma saudação

    Boa-madrugada: 0-5h
    Bom-dia: 6-12h
    Boa-tarde: 13-18h
    Boa-noite: 19-00h

'''

# Entrada
hora = input('Insira a hora: ')

try:
    hora = int(hora)
except:
    hora = input('Insira um numero correto entre 00 e 23!')

if hora >= 0 and hora <= 5: # Boa madrugada
    print('Boa Madrugada!')

elif hora >= 6 and hora <= 12: # Bom dia
    print('Bom dia!')

elif hora >= 12 and hora <= 19: # Boa tarde
    print('Boa tarde!')

elif hora >= 19 and hora <= 24: # Boa noite
    print('Boa noite!')

elif hora >= 25: #Hora incorreta
    print('Hora incorreta!')