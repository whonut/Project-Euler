import time
start=time.time()
def isPrime(n):
    sqrtn=n**0.5
    if  n==2:
        return True
    if  n % 2==0:
        return False
    if  n<2:
        return False
    for x in range(3,int(sqrtn)+1, 2):
        if  n % x==0:
            return False
    return True

#Solution 1
primes=[2,]
n=3

while primes[-1]<2000000:
    if isPrime(n):
        primes.append(n)
    n+=1

print sum(primes[:-1])

#Solution 2
#def get_primes(n):
#    while n<2000000:
#        if isPrime(n):
#            yield n
#        n+=1
#print sum(get_primes(1))
print time.time()-start
