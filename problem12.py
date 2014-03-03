from math import sqrt
from time import time
start=time()
def factor(n):
    factors=[1,n]
    for x in xrange(2,int(sqrt(n))+1):
        if n%x==0:
            factors.append(x)
            if n/x!=x:
                factors.append(n/x)
    return factors
divisors=0
number=None
n=1
while divisors<500:
    if len(factor(0.5*(n**2+n)))>divisors:
        divisors=len(factor(0.5*(n**2+n)))
        number=0.5*(n**2+n)
    n+=1
print number
print str(time()-start),'seconds'        
        
