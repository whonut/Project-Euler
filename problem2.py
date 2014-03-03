#Solution 1
evens=[]
fibs=[0,1]
while fibs[-1]+fibs[-2]<4000000:
    fibs.append(fibs[-1]+fibs[-2])
for item in fibs:
    if  item%2==0:
        evens.append(item)
print sum(evens)

#Solution 2
fibs=[0,1]
while fibs[-1]+fibs[-2]<4000000:
    fibs.append(fibs[-1]+fibs[-2])
print sum(n for n in fibs if n%2==0)


