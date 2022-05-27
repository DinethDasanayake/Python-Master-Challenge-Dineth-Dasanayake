import random

l = []

for i in range(100):
    i += 1
    l.append(random.randint(0, 100))

print(l)

unique = []

for x in l:
    if x not in unique:
        unique.append(x)

print("\nUnique elements list")
print(unique)

unique.reverse()
print("\nReversed Unique elements list")
print(unique)
