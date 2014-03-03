import pylab

sum_digits_raised=[]
linear=[]

for i in range(500000):
    sum_digits_raised.append(sum(int(d)**5 for d in str(i)))
    linear.append(i)

pylab.plot(sum_digits_raised, label='Sum of digits to the fifth power')
pylab.plot(linear, label='linear')
pylab.legend(loc = 'upper left')
pylab.figure()

pylab.show()

