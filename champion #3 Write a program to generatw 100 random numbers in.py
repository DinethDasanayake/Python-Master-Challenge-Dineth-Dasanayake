import random

l=[]
for i in range(100):
    i=random.randint(0,100)
    l.append(i)
    factors = 0  
    for divisible_number in range(i):
        divisible_number += 1 
        remainder = i % divisible_number
        if remainder == 0:
            factors += 1 
    if factors <= 2:
        print(i)
    else:
        pass
