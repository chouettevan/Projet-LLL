from typing import Self
"""
Le module mod permet de convertir un objet mathématique en un objet modulo un autre.
"""

class Modulo():
    """
    Classe représentant un objet modulo n
    """
    def __init__(self,objet,mod):
        self.objet = objet % mod
        self.mod = mod

    def __add__(self,other:Self) -> Self:
        """
        addition modulo n
        """
        return (self.objet  + other.objet) % self.mod

    def __sub__(self,other:Self) -> Self:
        """
        soustrction modulo n
        """
        return (self.objet - other.objet) % self.mod

    def __floordiv__(self,other:Self) -> Self:
        """
        division (tronquée) modulo n
        """
        return (self.objet // other.objet) % self.mod

    def __mul__(self,other:Self|int) -> Self:
        """
        multiplication modulo n
        """
        if type(other) != Modulo:
            return (self.objet * other) % self.mod
        return (self.objet * other.objet) % self.mod
    def __rmul__(self,other:Self|int) -> Self:
        """
        multiplication modulo n
        """
        return self*other

    def __pow__(self,other:Self) -> Self:
        """
        puissance modulo n
        """
        result = self
        for i in range(int(other)):
            result *= self
        return result

    def __neg__(self):
        """
        négation modulo n
        """
        return -1*self

    def __eq__(self,other) -> bool:
        """
        égalité mod n
        """
        return (self.objet == other.objet and self.mod == other.mod)

    def __str__(self):
        """
        représentation textuelle
        """
        return '{} (mod {}'.format(str(self.objet),str(self.mod))	

	
		
