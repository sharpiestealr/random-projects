def traduz(lista, dict):
    count = 0
    while (count != len(lista)):
        port[count] = dict(lista[count])
        count +=1
    return port

lista = ['blackberry', 'cherry', 'plum', 'apple', 'pineapple']
eng2port = {'pineapple': 'abacaxi', 'plum': 'ameixa', 'blackberry': 'amora', 'apple': 'maçã', 'cashew': 'caju', 'cherry': 'cereja'}

print(traduz(lista, eng2port))

#dic not callable???