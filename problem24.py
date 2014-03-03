#Solution 1 - cheating
#import itertools
#print ''.join(list(itertools.permutations('0123456789'))[999999])

#Solution 2
import math
n=1000000
digits=[0,1,2,3,4,5,6,7,8,9]

result=''
for i in range(10)[::-1]:
    m=n/math.factorial(i)
    n%=math.factorial(i)
    result+=str(digits[m])
    digits.pop(m)
print result



        

