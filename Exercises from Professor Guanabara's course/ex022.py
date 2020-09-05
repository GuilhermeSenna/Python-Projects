nome = input('Digite seu nome completo: ')
print(f'O nome com todas as letras maiúsculas é: {nome.upper()}')
print(f'O nome com todas as letras minusculas é: {nome.lower()}')
tamanho = len(nome)
espacos = nome.count(' ')
print(f'O tamanho do nome sem espaços é: {tamanho - espacos}')
parcial = nome.split()
print(f'O primeiro nome é: {parcial[0]}')





