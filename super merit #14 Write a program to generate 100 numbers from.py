import random
large=-100
small=100
for i in range(100):
    i=random.randint(-100,100)
    print(i)
    if large<i:
        large=i
    else:
        pass
    if small>i:
        small=i
    else:
        pass

dif=large-small
print("Largest number =",large)
print("Smallest number =", small)
print("Differece between the largest number & the smallest number =",dif)