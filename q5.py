def agrupa_por_idade(dicO):
    idade = {}
    numero = [dicO.values()]
    nome = [dicO.keys()]
    count = 0
    while (count != len(dicO)):
        if numero[count] in range (1, 12):
            idade['criança'] = nome[count]
        elif numero[count] in range (12, 18):
            idade['adolescente'] = nome[count]
        elif numero[count] in range (18, 60):
            idade['adulto'] = nome[count]
        else:
            idade['idoso'] = nome[count]
        count +=1
    return idade
