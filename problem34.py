import time
from math import factorial
start=time.time()

#Solution 1
#def factorion(n):
#    return sum(factorial(int(d)) for d in str(n))==n
#
#factorions=[]
#for n in range(3,10000000):
#    if factorion(n):
#        factorions.append(n)
#print sum(factorions)
#print time.time()

#Solution 2
factorials={str(i): factorial(i) for i in range(10)}
factorions=[]
def factorion(n):
    return sum(factorials[d] for d in str(n))==n
for n in range(3,10000000):
    if factorion(n):
        factorions.append(n)
print sum(factorions)
print time.time()-start

