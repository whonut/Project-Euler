def gcd(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a

cases = []
for i in xrange(10, 100):
    for j in xrange(10, 100):
        s_i = str(i)
        s_j = str(j)
        if s_i[1] == s_j[0]:
            if s_i[1] == '0':
                continue
            else:
                ans = float(i)/j
                try:
                    canceled = float(s_i[0])/float(s_j[1])
                except:
                    continue
                if ans == canceled:
                    cases.append((i, j))

num = 1
den = 1
for i, j in cases:
    num *= i
    den *= j
print den / gcd(num, den)
