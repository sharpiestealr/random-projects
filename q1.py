#inss
#>= 1045 - 7.5%, 1045.01-2089.6 -9%, 2089.61-3134.4 - 12%, 3134.41-6101.06 - 14%, 6101.06< - 671,12
#bc irrf
#bc = sal - inss - (dep*189.59)
#irrf
#irrf = bc*aliq-dedu
#if bc; aliq; dedu
    #até 1903.98; 0%; 0
    #1903.99-2826.65; 7,5%; 142.8
    #2826,66-3751,05; 15%; 354.8
    #3751.06-4664.68; 22.5%; 636.13
    #4664.68<; 27.5%; 869.36

#recebe sal e dep, imprime irrf

def Cinss(sal, dep):
    if sal <1045.01:
        taxa = 0.075
        inss = (sal * taxa)
    elif 1045.01 <= sal <= 2089.6:
        taxa = 0.09
        inss = (sal * taxa)
    elif 2089.61 <= sal <= 3134.4:
        taxa = 0.12
        inss = (sal * taxa)
    elif 3134.41<= sal <= 6101.06:
        taxa = 0.14
        inss = (sal * taxa)
    else:
        inss = 671.12
    return inss

def Cbc(sal, inss, dep):
    bc= sal - inss - (dep*189.59)
    return bc

def Cirrf(bc):
    if bc <=1903.98:
        aliq = 0
        dedu = 0
    elif 1903.99<= bc <= 2826.65:
       aliq = 0.075
       dedu = 142.8
    elif 2826.66<= bc <= 3751.05:
        aliq = 0.15
        dedu = 354.8
    elif 3751.06<= bc <= 4664.68:
        aliq = 0.225
        dedu = 636.13
    else:
       aliq = 0.275
       dedu = 869.36

    irrf = bc*aliq-dedu
    return irrf

sal = float(input("Informe aqui o seu salário bruto. \n"))
dep = int(input("Informe aqui o número de dependentes que você tem. \n"))
inss = Cinss(sal, dep)
bc = Cbc(sal, inss, dep)
irrf = Cirrf(bc)
print(irrf)