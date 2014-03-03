#01/01/1901 was a Tuesday
#(day)%7=6 if day is a Sunday where 01/01/1901=1
import time
start=time.time()
sundays=0
day=1
year=1901
#Solution 1
#def check(days):
#    if days%7==6:
#        global sundays
#        sundays+=1
#
#while year<2001:
#    check(day)
#    day+=31         #January
#    check(day)
#    if year%4==0:   #February 
#        day+=29
#    else:
#        day+=28
#    check(day)      
#    day+=31         #March
#    check(day)      
#    day+=30         #April
#    check(day)
#    day+=31         #May
#    check(day)
#    day+=30         #June
#    check(day)
#    day+=31         #July
#    check(day)
#    day+=31         #August
#    check(day)
#    day+=30         #September
#    check(day)
#    day+=31         #October
#    check(day)
#    day+=30         #November
#    check(day)
#    day+=31         #December
#    year+=1

#Solution 2
norm=[31,28,31,30,31,30,31,31,30,31,30,31]
leap=[31,29,31,30,31,30,31,31,30,31,30,31]
while year<2001:
    if year%4==0:
        L=leap
    else:
        L=norm
    for m in L:
        day+=m
        if day%7==6:
            sundays+=1
    year+=1

print sundays
print time.time()-start

        



