import random

n1 = random.randint(1, 10000)
n2 = random.randint(1, 10000)

print("number 1 =", n1)
print("number 2 =", n2)
if n1 < n2:
    print("number 1 is smaller")
elif n2 < n1:
    print("number 2 is smaller")
else:
    print("Both are equal")
