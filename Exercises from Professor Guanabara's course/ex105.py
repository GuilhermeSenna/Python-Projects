def notas(*notas, sit=False):
    quant = 0
    soma = 0
    semestre = {}
    for valor in notas:
        soma += valor
        quant += 1
    semestre['total'] = quant
    semestre['maior'] = max(notas)
    semestre['menor'] = min(notas)
    semestre['media'] = soma/quant
    if(sit == True):
        if semestre['media'] < 5:
            semestre['situacao'] = 'Ruim'
        elif semestre['media'] >= 5 and semestre['media'] < 7:
            semestre['situacao'] = 'Razoavel'
        elif semestre['media'] >= 7 and semestre['media'] < 8:
            semestre['situacao'] = 'Boa'
        else:
            semestre['situacao'] = 'Excelente'

    return semestre

# Programa Principal
resp = notas(7.5, 9.5, 10, 6.5, sit = True)
print(resp)