def verifica_lista(lista):
    count = 0
    lis = []
    resposta = "misturado"
    while (count != len(lista)):
        lis[count] = int(lista[count])
        count +=1
    count = 0
    while (count != len(lista)) and (len(lista) > 0):
        if ((lis[count]%2) == 0) and ((lis[count])!=0):
            resposta = "par"
        elif ((lis[count]%2) > 0) and ((lis[count])!=0):
            resposta = "ímpar"
        else:
            resposta = "misturado"
        count +=1
    return resposta

#l6, list assignment index out of range