import math
import cmath
from collections.abc import Callable

def sum(func:Callable[[complex],complex],a:int,b:int) -> complex:
    """
    prodède à la somme d'une fonction entre a et b
    """
    total = 0
    for i in range(a,b+1):
        total += func(i)
    return total

def integral(func:Callable[[float],complex],a:float,b:float,delta:float =0.001) -> complex:
    """
    intègre une fonction entre a et b
    """
    total = 0
    x = a
    while x < b:
        total += func(x)*delta
        x += delta
    return total

def fourier_transform(func:Callable[[float],float],delta:float=0.001,n:int=1000) -> Callable[[float],complex]:
    """
    transformée de fourier de f
    """
    def t1(e):
        def t2(x):
            return func(x) * cmath.exp(-cmath.sqrt(-1)*2*math.pi*e*x)
        return t2
    def transform(freq):
        return integral(t1(freq),-n,n,delta)
    return transform

