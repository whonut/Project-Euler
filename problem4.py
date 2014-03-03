import time
start=time.time()
def isPal(num):
        string=str(num)
        if len(string)<=1:
                return True
        else:
                return string[0]==string[-1] and isPal(string[1:-1])



pals=[]
for x in range(100,1000):
        for y in range(100,1000):
                if isPal(x*y):
                        pals.append(x*y)
print max(pals)
print time.time()-start


