def classifica_lista(lista):
    if len(lista) <= 2:
        resposta = "nenhum"
    elif lista == sorted(lista):
        resposta = "crescente"
    elif lista == sorted(lista, reverse = True):
        resposta = "decrescente"
    else:
        resposta = "nenhum"
    return resposta

#Condição do primeiro if está invertida. Deveria ser < 2.
#Não deveria usar o sorted.