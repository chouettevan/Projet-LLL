"""
Module servant à factoriser des polynômes,que ce soit dans les entier ou mod q.
Les polynômes sont  représentés par des tableaux, de sorte que
[1, 6 ,4, 3] correspond à 3x³ + 4x² + 6x + 1
"""

def evaluer(polynome:list,x:int) -> int:
    """
    évalue le polynôme en x
    """
    resultat = 0
    puissance = 1
    for i in range(x):
        resultat += puissance*polynome[i]
        puissance *= x
    return resultat

def isIrreductibleZ(polynome: list) -> bool:
    """
    tente de trouver un facteur de degré 1 à un polynôme (dans les entiers)
    Retourne True si le polynôme est irréductible
    """
    if polynome[0] == 0:
        return False
    c = polynome[0]
    for i in range(-c,c):
        if evaluer(polynome,i) == 0:
            return False
    return True

def isIrreductibleMod(polynome: list,mod:int) -> bool:
    """
    tente de trouver un facteur de degré 1 dans un polynôme (mod n)
    Retourne True si le polynôme est irréductible
    """
    if polynome[0] % mod == 0:
       return False
    for i in range(mod):
        if evaluer(polynome,i) % mod == 0:
            return False
    return True
