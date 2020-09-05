from time import sleep
import emoji
print('Contagem para os fogos:')
for x in range(10, 0, -1):
    print(x)
    sleep(1)
print(emoji.emojize(":fireworks::fireworks::fireworks:", use_aliases= True))