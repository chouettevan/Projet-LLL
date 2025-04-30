import sys
import matplotlib.pyplot as plt
import math
import cython
from cython.parallel import prange
s = 20
e = 1000

def show(a,b,c):
    txt = ''
    if a != 0:
        txt += f'{a}x² '
    if b != 0:
        txt += f'+ {b}x '
    if c != 0:
        txt += '+ ' + str(c)
    return txt

def factorZ(a:cython.int,b:cython.int,c:cython.int):
    r : cython.int
    r = 0
    i : cython.int
    i = 0
    if c == 0:
        return True
    for i in prange(-c,c+1,nogil=True):
        if a*(i**2) + b*i + c == 0:
            r = 1
            break
    if r == 1:
        return True
    else:
        return False


primes = []
for i in range(2,10000):
    prime = True
    for j in primes:
        if j * j > i:
            break
        if i % j  == 0:
            prime = False
            break
    if prime:
        primes.append(i)

def factorMod(a:cython.int,b:cython.int,c:cython.int,p:cython.int):
    a = a % p
    b = b % p
    c = c % p
    r : cython.int
    r = 0
    i : cython.int
    i = 0
    if c == 0:
        return True
    for i in prange(p,nogil=True):
        if (a*(i**2) + b*i + c) % p == 0:
            r = 1
            break
    if r == 1:
        return True
    else:
        return False
x = []
y = []
primes.remove(2)
nb = 0
tot = 0
for a in range(1,2):
    for b in range(s,e):
        for c in range(s,e):
            if not factorZ(a,b,c):
                tot += 1
                for i in primes:
                    if not factorMod(a,b,c,i):
                        nb += 1
                        if not i in x:
                            x.append(i)
                            y.append(0)
                        idx = x.index(i)
                        y[idx] += 1
                        break
print(nb,tot)

y2 = [math.log(i) for i in y] 

plt.plot(x,y2,'o')
plt.show()
