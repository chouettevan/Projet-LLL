
class Modulo():
    def __init__(self,objet,mod):
        self.objet = objet % mod
        self.mod = mod

    def __add__(self,other):
        return (self.objet  + other.objet) % self.mod

    def __sub__(self,other):
        return (self.objet - other.objet) % self.mod

    def __floordiv__(self,other):
        return (self.objet // other.objet) % self.mod

    def __mul__(self,other):
        if type(other) != Modulo:
            return (self.objet * other) % self.mod
        return (self.objet * other.objet) % self.mod
    def __rmul__(self,other):
        return self*other

    def __pow__(self,other):
        result = self
        for i in range(int(other)):
            result *= self
        return result

    def __neg__(self):
        return -1*self

    def __eq__(self,other):
        return (self.objet == other.objet and self.mod == other.mod)

    def __str__(self):
        return '{} (mod {}'.format(str(self.objet),str(self.mod))	

	
		
