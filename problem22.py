import time
from string import ascii_uppercase
start=time.time()
f=open('/Users/dylanevans/Documents/Computer_Stuff/Code/Project_Euler/problem22.txt')
names=f.read().replace('"','').split(',')
names.sort()
letter_score={c: ascii_uppercase.index(c)+1 for c in ascii_uppercase}

total=0
for n in names:
    score=0
    for c in n:
        score+=letter_score[c]
    total+=score*(names.index(n)+1)
print total
print time.time()-start
