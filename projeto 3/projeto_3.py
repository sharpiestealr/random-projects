import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
import math
 
m = 70 #massa em kg
a = 9.80665 #m/s²
cd = 0.82 #coeficiente de arrasto de um cilindro (pessoa)
Ap = 0.6 #Dados experimentais/medidos (considerando uma altura de uma pessoa de 1,75 m como a média)
Apa = 25 #area do paraquedas em m²
P = m*a

dt = 0.1
tempo = np.arange(0, 300, dt)
v0 = 0 #velocidade inicial
y0 = 3000 #altura inicial
ci = [y0, v0]

def modelo(lista, tempo): #com paraquedas
    y = lista[0]
    Vy = lista[1]
   
    cd = 0.82
    Ap = 0.6
    if y <= 1372: #altura da abertura do paraquedas
        cd = 1.75 #coeficiente de arrasto do paraquedas (nasa)
        Ap = Apa
    d = 1.225*math.e**(-y/7500)
    dydt = Vy
    dvydt = (- P +(1/2 * cd * d * Ap * Vy**2))/m
   
    if y <= 0:
        dydt = 0
        dvydt = 0
       
    return [dydt, dvydt]

def modelo2(lista, tempo): #sem paraquedas
    y = lista[0]
    Vy = lista[1]
   
    cd = 0.82
    Ap = 0.6
    d = 1.225*math.e**(-y/7500)
    dydt = Vy
    dvydt = (- P +(1/2 * cd * d * Ap * Vy**2))/m
   
    if y <= 0:
        dydt = 0
        dvydt = 0
       
    return [dydt, dvydt]

#VALIDAÇÂO
dt2 = 1
tempo2 = np.arange(0,300, dt2)
i=0
velocidade =[0]*300
for i in velocidade:
    velocidade.append(55)
#velocidade = [0,3,9,14,18,23,29,34,39,42,45,48,50,51,53,54]
#while i < len(velocidade):
  #  velocidade.append(55)
   # i+=1

S = odeint(modelo, ci, tempo)
R = odeint(modelo2, ci, tempo)

print(S)
print(R)

plt.plot(tempo,  R[:,0], label="sem paraquedas")
plt.plot(tempo, S[:,0], label= "com paraquedas") #altura por tempo
plt.legend()
plt.show()

#plot.plot(tempo, S[:,1], label="com paraquedas") #velocidade por tempo
#plt.plot(tempo, R[:,1], label="sem paraquedas")
#plt.show()

plt.plot(- S[:,0], -S[:,1], label="com paraquedas")
plt.plot(-R[:,0],- R[:,1],label="sem paraquedas")
plt.legend()
plt.show()
