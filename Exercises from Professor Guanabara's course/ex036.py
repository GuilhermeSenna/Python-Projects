valor = int(input('Qual o valor total a ser pago na casa? '))
salario = int(input('Qual o seu salário mensal? '))
anos = int(input('Em quantos anos pretende pagar o valor total da casa?'))
prestacao = valor/(anos*12)
minimo = salario * 0.3
if prestacao > minimo:
    print('A transacao não pode ser aceita por ser acima de 30% de seu salário.')
    print(f'Prestacao mensal {prestacao}, 30% do salario {minimo}')
else:
    print('A transacao foi aceita com sucesso.')
