frase = 'A aranha arranha a jarra'.lower()
contador = frase.count('a')
primeira = frase.find('a')
ultima = frase.rfind('a')
print(f'A letra "a" aparece {contador} vezes.')
print(f'A letra "a" aparece a primeira vez na {primeira+1}ª posição.')
print(f'A letra "a" aparece pela ultima vez em {ultima+1}ª posição.')