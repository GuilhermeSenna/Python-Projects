distancia = int(input('Digite a distancia de sua viagem (em km): '))
if distancia <= 200:
    print(f'O valor a ser pago é {distancia*0.5} reais.')
else:
    print(f'O valor a ser pago é {distancia*0.45} reais.')
