#class Foguete
#init: speed km/h
#atualizar(t[s])=space that the rocket moved since last update in km

class Foguete(object):
    def __init__(self, velocidade):
        self.speed = velocidade
        self.pos = 0
    def atualizar(self, tempoS):
        space = (self.speed/3.6)*(tempoS)/1000
        self.pos = self.pos + space
        return self.pos

foguete = Foguete(10000)
f9 = foguete.atualizar(9)
f18 = foguete.atualizar(18)
print(f9)
print(f18)