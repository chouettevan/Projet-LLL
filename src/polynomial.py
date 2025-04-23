
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

def factorZ(polynome: list) -> bool:
    """
    tente de trouver un facteur de degré 1 à un polynôme (dans les entiers)
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
    """
    if polynome[0] % mod == 0:
       return False
    for i in range(mod):
        if evaluer(polynome,i) % mod == 0:
            return False
    return True
