import random

l=[]

for i in range(50):
    i=random.randint(-100,100)
    l.append(i)

print(l)


l.sort()
l.reverse()
print("\nAfter sorting")
print(l)

