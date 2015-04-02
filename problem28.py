from itertools import cycle


translations = cycle(((1, 0), (0, -1), (-1, 0), (0, 1)))
current_trans = None
p = (0, 0)
n = 1
sum = 0

while n < 5 * 5:
    if abs(p[0]) == abs(p[1]) or n == 2:      # p is on a diagonal
        print p, n        
        sum += n
        current_trans = next(translations)        
        p = (p[0] + current_trans[0], p[1] + current_trans[1])
    else:
        p = (p[0] + current_trans[0], p[1] + current_trans[1])
    n += 1

print sum
