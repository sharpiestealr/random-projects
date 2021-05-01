#bhaskara
#sinx = (4x(180-x))/(40500-(x(180-x)))
#x entre 0 e 90o
#Desenvolva um programa que imprima o ponto de maior erro da função de Bhāskara.
#Para isso, para os valores de 0 a 90 graus, de um e um grau, analise a diferença da função de Bhāskara em relação a função math.sin do Python 
#e diga qual é o valor em graus que o valor de seno apresenta a maior diferença entre ambas as técnicas
#Você provavelmente vai querer usar a função abs()

import math

def diferença():
    dif = {}
    count = 0
    while (count <= 90):
        dif[count] = abs((4*count(180-count))/(40500-(count(180-count)))-math.sin(degrees(count)))
        print(count, dif[count]) #esse print nem printa nada então o erro tá antes
                                 #mas sinceramente não faço ideia de qual seja
        count +=1
    auge = max(dif.values)
    return dif[auge]

print(diferença)

#NÃO TÁ RETORNANDO VALOR ALGUM ???????????