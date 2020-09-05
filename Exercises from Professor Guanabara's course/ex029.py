velocidade = int(input('Digite a velocidade atual do carro(Km/h): '))
if velocidade <= 80:
    print(f'Parabéns por respeitar a velocidade permitida ({velocidade}km/h), mantenha-se no limite.')
else:
    multa = (velocidade-80)*7
    print(f'Você ultrapassou a velocidade permitida de 80km/h, sua velocidade é {velocidade}km/h\nSua multa sera de {multa} reais.')
