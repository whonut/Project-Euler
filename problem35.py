from math import factorial as fac


def isPrime(n):
    if n == 4:
        return False
    if fac(n-1) == -1 % n:
        return True
        

def isCirc(n):
    digits = str(n).split()
    l = len(digits)
    cycles = [digits[i-j].join('') for i in xrange(l) for j in xrange(l)]
    rotations = map(int, cycles)
    for r in rotations:
        if not isPrime(r):
            return False
    if len(s) > 1:
        if s[1] == '0':
            return False
    return True

circs = 0
for i in xrange(1, 1000000):
    print i
    if isCirc(i):
        circs += 1

print circs
