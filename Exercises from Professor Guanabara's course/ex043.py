peso = int(input('Digite seu peso: '))
altura = int(input('Digite sua altura: '))
imc = peso/pow(altura,2)
if imc < 18.5:
    print('Seu status é: Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print('Seu status é: Peso ideal.')
elif 25 <= imc < 30:
    print('Seu status é: Sobrepeso.')
elif 30 <= imc < 40:
    print('Seu status é: Obesidade.')
else:
    print('Seu status é: Obesidade mórbida.')
