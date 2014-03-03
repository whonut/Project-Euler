import time


#Solution 1
#start=time.time()
#def specialTriple():
#    for a in range(1,1000):
#        for b in range(a+1,1000):
#            for c in range(b+1,1000):
#                if c**2==a**2+b**2 and a+b+c==1000:
#                    print 'triple is:',(a,b,c)
#                    print 'product=',str(a*b*c)
#                    print str(time.time()-start)
#                    return


#Solution 2
start=time.time()
def factorPairs(n):
    factors=[(n,1)]
    for x in xrange(2,int(n**0.5)+1):
        if n%x==0:
            factors.append((n/x,x))
    return factors

def specialTriple():
    for k in range(1,499):
        if k%2!=0:
            k*=2
        for pair in factorPairs(k/2):
            m,n=pair
            a,b,c=(m**2-n**2),k,(m**2+n**2)
            if a+b+c==1000:
                print 'triple is:',(a,b,c)
                print 'product=',str(a*b*c)
                print time.time()-start
                return

specialTriple()

      

        


