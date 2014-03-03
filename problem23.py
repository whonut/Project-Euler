#Solution 1
import time
start=time.time()
def factor(n):
    factors=[1,]
    for x in xrange(2,int(n**0.5)+1):
        if n%x==0:
            factors.append(x)
            if n/x!=x:
                factors.append(n/x)
    return factors

abundants=[12,]
for i in xrange(13,28124):
    if sum(factor(i))>i:
        abundants.append(i)

i=0
nums={i:True for i in xrange(1,28124)}
while i<len(abundants)-1:
    j=i
    while abundants[i]+abundants[j]<28124:
        if nums[abundants[i]+abundants[j]]:
            nums[abundants[i]+abundants[j]]=False
        j+=1
    i+=1
print sum(i for i in nums.keys() if nums[i])
print time.time()-start



