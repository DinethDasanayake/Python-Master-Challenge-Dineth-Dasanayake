x = 0
y = 1
z = 2
t = 3
for x in range(100):
    x += 1
    y += 1
    z += 1
    t += 1
    if t == z+y:
        print(t)
