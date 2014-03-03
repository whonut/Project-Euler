#Solution 1
nums=[]
for n in range(2,194980):
    sum_digits_raised=sum(int(d)**5 for d in str(n))
    if sum_digits_raised==n:
        nums.append(n)
print sum(nums)


