best_i = None
longest_cycle = 0


def long_div(n, m, calls=0, prev_remainders=None):
    '''Divides n by m and returns length of repetend'''
    if prev_remainders is None:
        prev_rems = []

    result = ''
    remainder = n % m
    while remainder not in prev_rems and remainder != 0:
        prev_rems.append(remainder)
        print prev_rems
        n = remainder * 10
        print '{}/{}'.format(n, m)
        result = result + str((n-remainder)/m)
        print result
        remainder = n % m
#     if remainder == 0:
#         return 0
#     else:
#         return len(result)

# for i in xrange(1, 1000):
#     div = long_div(1, i)
#     # print i, div
#     if div > longest_cycle:
#         longest_cycle = div
#         best_i = i
