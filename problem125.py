from math import sqrt
from time import time


def isPal(num):
        string = str(num)
        if len(string) <= 1:
                return True
        else:
                return string[0] == string[-1] and isPal(string[1:-1])


def memoize(f):
    cache = {}

    def decorated_function(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorated_function


# memoise - conseq from
def ConseqSquares(n):
    if int(sqrt(n)) == sqrt(n):
        return False

    for i in xrange(1, int(sqrt(n))):
        sum = 0
        m = i
        while sum < n:
            sum += m ** 2
            m += 1
        if sum == n:
            return True
    return False

nums = []
start = time()
for n in xrange(10, 10**8):
    if n % 10**6 == 0:
        print n
        print 'dt =', str(time() - start)
        start = time()
    if isPal(n) and ConseqSquares(n):
        nums.append(n)

print sum(nums)
