n = s = digitados = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    digitados += 1
    s += n
print(f'A quantidade de numeros digitados foi'
      f' {digitados} e a soma vale {s}.')
