def gcd(a,b):
    while a!=b:
        if a<b:
            b=b-a
        else:
            a=a-b
    return a

def lcm(*nums):
    if len(nums)==2:
        return (nums[0]/gcd(nums[0],nums[1]))*nums[1]
    else:
        return reduce(lcm,nums)


print lcm(*range(1,21))
