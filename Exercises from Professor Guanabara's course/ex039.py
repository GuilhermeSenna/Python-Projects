idade = int(input('Digite sua idade atual: '))
if idade < 18:
    print(f'Ainda não é a hora certa, faltam {18-idade} anos, para você se alistar.')
elif idade == 18:
    print('Está no momento de você se alistar, corra até o posto de alistamento mais próximo.')
else:
    print(f'Você já passou do prazo de alistamento há {idade-18} anos, procure se alistar o mais depressa possível.')