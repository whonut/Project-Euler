def isPrime(n):
    if  n==2:
        return True
    if  (n % 2 == 0) or (n < 2) :
        return False
    sqrtn=n**0.5    
    for x in range(3,int(sqrtn)+1, 2):
        if  n % x==0:
            return False
    return True

best = (None, None)
best_conseq = 0 

for a in xrange(-999, 1000):
    for b in xrange (-999, 1000):
        print '(' + str(a) + ',', str(b) + ')'
        conseq = 0
        n = 0
        while isPrime(n**2 + a*n + b):
            conseq += 1
            n += 1
        if conseq > best_conseq:
            best_conseq = conseq
            best = (a, b)

print best[0]*best[1]

