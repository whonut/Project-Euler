import math
#Solution 1
#def isPrime(n):
#    sqrtn=n**0.5
#    if  n==2:
#        return True
#    if  n % 2==0:
#        return False
#    if  n<2:
#        return False
#    for x in range(3,int(sqrtn)+1, 2):
#        if  n % x==0:
#            return False
#    return True
#primes=[]
#factors=[]
#for n in range(2,int(600851475143**0.5)+1):
#    if  isPrime(n):
#        primes.append(n)
#for e in primes:
#    if  600851475143%e==0:
#        factors.append(e)
#print factors[-1]

#Solution 2
div=2
num=600851475143
factor=0
while div<=600851475143**0.5:
    if num%div==0:
        factor=div
        num/=div
    else:
        div+=1
print factor


