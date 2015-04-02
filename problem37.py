def isPrime(n):
    sqrtn = n ** 0.5
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n < 2:
        return False
    for x in range(3, int(sqrtn) + 1, 2):
        if n % x == 0:
            return False
    return True


def isTrunct(n, start):
    s = str(n)
    if len(s) == 1:
        return isPrime(n)
    else:
        if start == 'R':
            return isPrime(n) and isTrunct(int(s[:-1]), 'R')
        else:
            return isPrime(n) and isTrunct(int(s[1:]), 'L')

truncts = []
n = 8
while len(truncts) < 11:
    if isTrunct(n, 'R') and isTrunct(n, 'L'):
        print n
        truncts.append(n)
        print len(truncts)
    n += 1

print sum(truncts)
