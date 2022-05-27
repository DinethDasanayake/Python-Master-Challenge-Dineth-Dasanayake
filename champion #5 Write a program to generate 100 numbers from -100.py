import random

l = []
for i in range(100):
    i += 1
    l.append(random.randint(-100, 100))

print(l)
l.sort()
print("Minimum two :", l[0], ",", (l[1]))
print("Maximum two :", l[99], ",", (l[98]))
