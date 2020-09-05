dias = int(input('por quantos dias o carro foi alugado: '))
km = float(input('Quantos kms foram percorridos com o carro: '))
print('{} dias e {} kms rodados totalizam: {:.2f} reais '.format(dias, km, dias*60 + km*0.15))
