import random

l=[]

for i in range(30):
    i=random.randint(-100,100)
    l.append(i)

print(l)
print("\nAfter sorting")
l.sort()
print(l)

