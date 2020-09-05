salario = int(input('Digite seu salário atual: '))
if salario > 1250:
    print(f'Seu salario atual é {salario} reais, com o aumento de 10% você receberá {salario*1.1} reais.')
else:
    print(f'Seu salario atual é {salario} reais, com o aumento de 15% você receberá {salario*1.15} reais.')
