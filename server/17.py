def eh_bissexto(ano):
    if (ano %4 == 0 and ano %100 != 0) or (ano %400 == 0):
        return True
    else:
        return(ano %4 == 0)

# server crying because 1 is "supposed to be a leap year" but ??????????????
