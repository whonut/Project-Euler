#Solution 1
seq=[]
for a in xrange(2,101):
    for b in xrange(2,101):
        if not a**b in seq:
            seq.append(a**b)
print len(seq)

#Solution 2
#TODO generator
