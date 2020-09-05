vazio = ''
cinq = vinte = dez = um = 0
print(f'{vazio:=^50}\n \t\t\t\tCAIXA ELETRONICO\n{vazio:=^50}')
valor = int(input('Qual o valor que deseja sacar: '))
while valor <= 0:
    valor = int(input('Digite um valor valido: '))
cinq = valor // 50
valor = valor % 50
vinte = valor // 20
valor = valor % 20
dez = valor // 10
valor = valor % 10
um = valor

if cinq != 0:
    print(f'Total de {cinq} cedulas de R$50')
if vinte != 0:
    print(f'Total de {vinte} cedulas de R$20')
if dez != 0:
    print(f'Total de {dez} cedulas de R$10')
if um != 0:
    print(f'Total de {um} cedulas de R$1')