import time
start=time.time()
fibs=[1,1]
while len(str(fibs[-1]))<1000:
    fibs.append(fibs[-2]+fibs[-1])
print len(fibs) 
print time.time()-start
