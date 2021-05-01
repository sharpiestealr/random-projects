from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
import math

## implemente sua função f(t) aqui
#def f(t):
#    f = t**2
#    return f


## implementação do gráfico da função f(t)
#arrT=np.arange(start=0, stop=10, step=0.01)
#fun = [0]*len(arrT)

#count = 0
#while (count != len(arrT)):
#    fun[count] = f(arrT[count])
#    count +=1

#plt.plot(arrT,fun)  
#plt.xlabel("Tempo")
#plt.ylabel("f(t)")
#plt.grid(True)
#plt.show()


## implemente a função TaxadeVariacao aqui
#def TaxadeVariacao(t, delta_t):
#    dx = ((f(t+1)-f(t)))/delta_t
#    return dx


## ERRADA
## implemente aqui o código que plota f(t) e df/dt
#arrT=np.arange(start=0, stop=10, step=0.01)
#y = [float(0)]*len(arrT)
#dT = [float(0)]*(len(arrT)-1)
#tx_var = [float(0)]*(len(arrT))

#count = 0
#while (count != len(arrT)-1):
#    dT[count] = arrT[count+1]-arrT[count]
#    count +=1

#del(y[-1])
#del(tx_var[-1])

#count = 0
#while (count != len(y)):
#    y[count] = f(arrT[count])
#    count +=1
    
#count = 0
#while (count != len(tx_var)):
#    tx_var[count] = TaxadeVariacao(arrT[count], dT[count])
#    count +=1
    
#del(y[-1])
#del(tx_var[-1])
    
#plt.plot(y, tx_var)  
#plt.xlabel("f(t)")
#plt.ylabel("dF/dT(t)")
#plt.grid(True)
#plt.show()


## FALTOU IMPLEMENTAR TX DE VARIAÇÃO DE F2 E F3
## suas implementações do item d) aqui
#def f2(t):
#    f2 = math.e**t
#    return f2

#def f3(t):
#    f3 = math.cos(t)
#    return f3


# implemente sua função "EquacaoDiferencial" aqui
def EquacaoDiferencial(y, t, a, w):
    dy_dt=a*y*(1+2*math.sin(w*t))
    return dy_dt

# implemente o código que usa a função EquacaoDiferencial e preenche a série temporal aqui
y = [float(5)]*400000
a = 0.007
w = 0.05
t = 0.001
jefferson = 0.001

count = 1
while (count != len(y)):
    y[count] = y[count-1] + (EquacaoDiferencial(y[count-1], jefferson, a, w)*t)
    jefferson = jefferson + t
    count +=1
    
print(y[365000])


y0 = 5

y = [float(5)]*400000
a = 0.007
w = 0.05
t = 0.001
jefferson = 0.001

count = 1
while (count != len(y)):
    y[count] = y[count-1] + (EquacaoDiferencial(y[count-1], jefferson, a, w)*t)
    jefferson = jefferson + t
    count +=1
    
t_lista = np.arange(0, 400, 0.001)
    
a_lista = odeint(EquacaoDiferencial, y0, t_lista, args = (a, w))

plt.plot(t_lista, a_lista, linewidth=5)  
plt.plot(t_lista, y, 'r')
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Solução do Modelo")
plt.grid(True)
plt.show()
