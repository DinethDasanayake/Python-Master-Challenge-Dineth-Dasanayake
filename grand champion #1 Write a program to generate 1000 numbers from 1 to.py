import random
l = []
sim = []
sum = 0
n = 0
for i in range(10):
    i = random.randint(0, 5)
    l.append(i)
print(l)
for i in range(100):
    i += 1
    if l[n] == l[i]:
        sim.append(l[n])
        n += 1
    else:
        n += 1

print(sim)
