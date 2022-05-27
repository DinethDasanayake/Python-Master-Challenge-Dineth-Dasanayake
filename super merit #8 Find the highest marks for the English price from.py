import random

high = -100
s = 0
for i in range(10):
    i = random.randint(0, 100)
    s += 1
    print(s, "th student :", i)
    if high < i:
        high = i
    else:
        pass

print("Highest Marks =", high)
