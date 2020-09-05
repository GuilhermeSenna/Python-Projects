#Checagem de parenteses
exp = str(input('Digite sua expressão: '))
if exp.count('(') == exp.count(')'):
    print('Sua expressão está válida.')
else:
    print('Sua expressão está inválida.')