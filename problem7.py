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

primes=[2,]
n=3
while len(primes)<10001:
    if isPrime(n):
        primes.append(n)
    n+=2

print primes[-1]
