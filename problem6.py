sum_squared=sum(range(1,101))**2
square_sum=0
for num in range(1,101):
    square_sum+=num**2

print abs(square_sum-sum_squared)
