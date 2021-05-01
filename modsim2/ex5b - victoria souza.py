#Exercício 5b 
#Victoria Souza - Turma B

import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import odeint

from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

l0 = 30/100
m = 200/1000
k = 10
g = 10
r = 10/100
Cd = 1.5
rho = 1
A = math.pi*r**2 

x0 = 55/100
dxdt = 0
y0 = 0
dydt = 0
ci = [x0, y0, dxdt, dydt]

def modelo(ci, t, check):
    x = ci[0]
    y = ci[1]
    vx = ci[2]
    vy = ci[3]
    
    d, v = (x**2+y**2)**(1/2), (vx**2+vy**2)**(1/2)
    el, ar, p = k*(d-l0), (rho*v**2*Cd*A)/2, m*g
    sin, cos = x/d, y/d

    dxdt, dydt = vx, vy

    if (check == True):
        d2xdt2 = (-el*sin-(ar*cos))/m
        d2ydt2 = (el*cos-(ar*sin)-p)/m

    else:
        d2xdt2 = (-el*sin)/m
        d2ydt2 = (el*cos-p)/m
    
    derivadas = [dxdt, dydt, d2xdt2, d2ydt2]

    return derivadas

tm, tM, dt = 0, 20, 1e-3

tempo = np.arange(tm, tM, dt)

no_res = odeint(modelo, ci, tempo, args=(False,))
res = odeint(modelo, ci, tempo, args=(True,))

x_no_res = no_res[:,0]
y_no_res = no_res[:,1]
x_res = res[:,0]
y_res = res[:,1]


plt.figure(1, (15, 7.5), 300)

plt.plot(y_no_res, x_no_res, label= "Sem resistência do ar", color = "magenta")
plt.plot(y_res, x_res, label= "Com resistência do ar", color = "red")
plt.title("Trajetória")
plt.legend(loc = "best")
plt.grid(True)
plt.xlabel("eixo y (m)")
plt.ylabel("eixo x (m)")

plt.figure(1, (15, 7.5), 300)

plt.plot(x_no_res, tempo, label= "Sem resistência do ar", color = "magenta")
plt.plot(x_res, tempo, label= "Com resistência do ar", color = "red")
plt.title("Abcissa")
plt.legend(loc = "best")
plt.grid(True)
plt.xlabel("tempo (μs)")
plt.ylabel("eixo x (m)")

plt.figure(1, (15, 7.5), 300)

plt.plot(y_no_res, tempo, label= "Sem resistência do ar", color = "magenta")
plt.plot(y_res, tempo, label= "Com resistência do ar", color = "red")
plt.title("Ordenada")
plt.legend(loc = "best")
plt.grid(True)
plt.xlabel("tempo (μs)")
plt.ylabel("eixo y (m)")

plt.show()