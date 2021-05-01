#PiWallis
#pi/2 = pares/ímpares * each other (2/1,2/3,4/3,4/5
#recebe número de argumentos pra calc pi

def PiWallis(num):
    mult = 1
    if (num%2) == 0:
        num = num + 1
        while (num > 0):
            mult = ((num+1)/num)*mult
            num -= 2
        mult=mult/2
    else:
        num = num + 1
        while (num > 0):
            mult = (num/(num-1))*mult
            num -= 2
    pi=(mult)*2
    return pi

#n=2 pi=2.6666 deu 4