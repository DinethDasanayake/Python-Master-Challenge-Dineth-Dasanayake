import random

l=[]
sum=0

for i in range(100):
    i+=1
    l.append(random.randint(0,100))

print(l)

unique=[]

for x in l:
    if x not in unique:
        unique.append(x)
    sum+=x

print("\nUnique elements")
print(unique)
print("Sum :",sum)
