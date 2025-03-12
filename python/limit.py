import math
def sum_approx(func,n=1000):
    total = 0
    for i in range(-n,n):
        total += func(i)
    return total

def integral_approx(func,a,b,delta=0.001):
    total = 0
    x = a
    while x < b:
        total += func(x)
        a += delta

def fourier_transform(func,delta=0.001,n=1000):
    def t1(e):
        def t2(x):
            return func(x) * math.exp(-sqrt(-1)*2*math.pi*e*x)
        return t2
    def transform(freq):
        return integral_approx(t1(freq),-n,n,delta)
    return transform

