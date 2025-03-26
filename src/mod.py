

class Modulo():
    def __init__(self,objet,mod):
        this.objet = objet % mod
    
    def __add__(self,other):
        return (self.objet  + other.objet) % mod

    def __mul__(self,other):
        return (self.objet * other.objet) % mod
