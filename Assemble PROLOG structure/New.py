cidades = []
inf = []
info = list(list())
aux = 1
empresa = 'aguia_branca'

fo = open("entrada.txt", "r")
line = fo.readlines()
for c in range(len(line)):
    line[c] = line[c].rstrip()
fo.close()
for c in range(len(line)):
    line[c] = line[c].replace('\t', '')
    for y in range(2):
        if line[c][0].isnumeric():
            line[c] = line[c].replace(line[c][0], '')
    line[c] = line[c].strip().lower()
    line[c] = line[c].replace('á', 'a').replace('à', 'a').replace('ã', 'a').replace('é', 'e').replace('â', 'a').replace('í', 'i').replace('ç', 'c').replace('ó', 'o').replace('ô', 'o').replace(' ', '_')
print(line)

linha = input('Digite o numero da linha: ')

cont = int(input('Digite a quantidade de horários disponíveis de ida: '))
for c in range(cont):
    inf.clear()
    inf.append(input('Digite o horario: '))
    inf.append(input('Digite os dias (digite separado): ').lower().replace(' ', ','))
    info.append(inf[:])
    # [ cidade_sol/"003"/"5:00h"/[dias], cidade_sol ... ]


print(f'linha({line[0]}, {line[len(line)-1]}, [', end='')
for k, v in enumerate(line):
    if k < len(line)-1:
        print(v, end=', ')
    else:
        print(v, end='')



for n in range(len(info)):
    if n == 0 and len(info)-1 == n:
        print(f'], [{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}]]).')
    elif n == 0 and len(inf) > 1:
        print(f'], [{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}], ', end='')
    elif n > 0 and len(info)-1 == n:
        print(f'{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}]]). ')
    else:
        print(f'{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}], ', end='')


cont = int(input('Digite a quantidade de horários disponíveis de volta: '))
info.clear()
for c in range(cont):
    inf.clear()
    inf.append(input('Digite o horario: '))
    inf.append(input('Digite os dias (digite separado): ').lower().replace(' ', ','))
    info.append(inf[:])

print(f'linha({line[len(line)-1]}, {line[0]}, [',end='')

line.reverse()

for k, v in enumerate(line):
    if k < len(line)-1:
        print(v, end=', ')
    else:
        print(v, end='')

for n in range(len(info)):
    if n == 0 and len(info)-1 == n:
        print(f'], [{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}]]).')
    elif n == 0 and len(inf) > 1:
        print(f'], [{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}], ', end='')
    elif n > 0 and len(info)-1 == n:
        print(f'{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}]]). ')
    else:
        print(f'{empresa}/"{linha}"/"{info[n][0]}"/[{info[n][1]}], ', end='')

# print(f'], [{empresa},"{linha}","{horida}"/{diaida}]).')
# print(f'linha({volta}, {ida}, [águia_branca,"{linha}","{horvol}"/{diavolta}]).')'''

# linha(bom_despacho,itacare,[bom_despacho,nazaré,valença,nilo_peçanha,ituberá,igrapiuna,camamu,itacare],[cidade_sol/"003"/"5:00h"/[seg,ter,qua],cidade_sol/"009"/"10:00h"/[seg,ter]]).