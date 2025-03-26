def pgcd(unsigned int a,unsigned int b):
    while a > 1 && b > 1:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 1 || b == 1:
        return 1
    if a == 0:
        return b
    if b == 0:
        return a
    return -1
