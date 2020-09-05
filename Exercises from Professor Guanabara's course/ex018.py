from math import sin, cos, tan, radians
ang = float(input('Digite o angulo desejado: (de preferencia 30,45 ou 60): '))
#print(f'O angulo de {ang} possui sen = {sin(radians(ang))}\nO angulo de {ang} possui cos = {cos(radians(ang))}\nO angulo de {ang} possui tag = {tan(radians(ang))}')
print('O angulo de {} possui sen = {:.2f}\nO angulo de {} possui cos = {:.2f}\nO angulo de {} possui tan = {:.2f}'.format(ang, sin(radians((ang))), ang, cos(radians(ang)), ang, tan(radians(ang))))
#O sin,cos,tan e demais funções matematicas funcionam com radiano, logo é usado o radians (da biblioteca math[...]
#[...]tambem), para transformar de graus para radianos.