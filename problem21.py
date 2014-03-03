from math import sqrt

def factor(n):
    factors=[1,]
    for x in xrange(2,int(sqrt(n))+1):
        if n%x==0:
            factors.append(x)
            if n/x!=x:
                factors.append(n/x)
    return factors

def d(n):
    return sum(factor(n))

amicables=[]

for n in range(1,10000):
    if d(d(n))==n and not n in amicables and n!=d(n):
        amicables.append(n)
        amicables.append(d(n))

print sum(amicables)
        
