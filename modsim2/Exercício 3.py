#imports
import matplotlib.pyplot as plt
import numpy as np
import math as math
from scipy.integrate import odeint

## Insira aqui seu código do item A-i
def f (t):
    ft = t**2
    return ft


## Insira aqui seu código do item A-ii
lista = np.arange(0, 10, 0.1)

for i in range (len(lista)):
    resultado = f(lista)
    
plt.plot(lista, resultado, c='purple')
plt.grid(true)
plt.show()


## Insira aqui seu código do item A-iii
def f_taxa(t, dt):
    for i in range (1, len(resultado)):
        taxa = (resultado[i] - resultado[i-1])/dt
    return taxa

## Insira aqui seu código do item A-iv
f_lista = [0] * (len(resultado))
f_taxa_lista = [0] * (len(resultado))

dt = 0.01

for i in range (0, len(resultado)):
    f_taxa_lista[i] = f_taxa(lista, dt)

del(f_lista[-1])

plt.plot(lista, f_taxa_lista, c='magenta')
plt.grid(True)

plt.show()

## Insira aqui seu código do item A-v
def g(t):
    gt = math.e**t
    return gt

def g_taxa(t, dt):
    taxa = g(t)/dt
    return taxa

def h(t):
    ht = math.cos(t)
    return ht

def h_taxa(t, dt):
    taxa = h(t)/dt
    return taxa

g_lista = [0] * (len(resultado))
g_taxa_lista = [0] * (len(resultado))
h_lista = [0] * (len(resultado))
h_taxa_lista = [0] * (len(resultado))

for i in range (0, len(lista)):
    g_lista[i] = g(lista)
    g_taxa_lista[i] = g_taxa(lista, dt)
    h_lista[i] = h(lista)
    h_taxa_lista[i] = h_taxa(lista, dt)

plt.figure(figsize = (7.5, 15))

plt.subplot(211)
plt.plot(g_lista, g_taxa_lista, c='orange')
plt.grid(True)

plt.subplot(212)
plt.plot(h_lista, h_taxa_lista, c='red')
plt.grid(True)

plt.show()

# Insira aqui seu código do item B-i
def modelo(y, t, a, w):
    dy_dt=a*y*(1+2*math.sin(w*t))
    return dy_dt

# Insira aqui seu código do item B-ii
y = [float(5)]*400000
a = 0.007
w = 0.05
t = 0.001

count = 1
while (count != len(y)):
    y[count] = y[count-1] + (modelo(y[count-1], (count*t), a, w)*t)
    count +=1

print("A população de bactérias após um ano ou 365 dias é: {0}.".format(y[365*1000]))


# Insira aqui seu código do item C
    
tempo = np.arange(0, 400, 0.001)

a_lista = odeint(modelo, y[5], tempo, args = (a, w))

plt.plot(tempo, a_lista, color = 'magenta', linewidth=8)  
plt.plot(tempo, y, color = 'purple', linewidth = 2)
plt.xlabel("tempo")
plt.ylabel("quantidade de bactérias")
plt.title("Solução do Modelo")
plt.grid(True)
plt.show()