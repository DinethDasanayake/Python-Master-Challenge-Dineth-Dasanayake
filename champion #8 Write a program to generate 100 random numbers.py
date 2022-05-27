import random

l = []

for i in range(100):
    i += 1
    l.append(random.randint(0, 100))

print(l)

unique = []
unique_odd = []
unique_even = []
for x in l:
    if x not in unique:
        unique.append(x)

for i in range(len(unique)-1):
    i += 1
    if unique[i]%2==0:
        unique_even.append(unique[i])
    else:
        unique_odd.append(unique[i])

print("\nUnique even integers")
print(unique_even)
print("\nUnique odd integers")
print(unique_odd)
