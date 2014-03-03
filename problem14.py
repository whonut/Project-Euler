from time import time
longest=0
number=None
cache={}
def collatz(n):
    m=n
    seq=1
    while n>1:
        if n<m:
            seq+=cache[n]
            break
        elif n%2==0:
            n/=2
        else:
            n=(3*n)+1
        seq+=1       
    cache[m]=seq
    return seq
start=time()
for x in range(2,1000001):
    if collatz(x)>longest:
        longest=collatz(x)
        number=x
print number
print str(time()-start),'seconds'


