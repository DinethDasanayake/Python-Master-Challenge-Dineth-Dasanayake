import random

n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2 :"))
n3 = int(input("Enter number 3 :"))

if n1 > n2:
    if n1 > n3:
        print(n1, " is the largest")
    else:
        pass
elif n2 > n1:
    if n2 > n3:
        print(n2, "is the largest")
    else:
        pass
elif n3 > n2:
    if n3 > n1:
        print(n3, "is the largest")
    else:
        pass
else:
    pass
n1 = random.randint(0, 10000)
n2 = random.randint(0, 10000)
n3 = random.randint(0, 10000)

print("Random number 1 =", n1)
print("Random number 2 =", n2)
print("Random number 3 =", n3)


if n1 > n2:
    if n1 > n3:
        print(n1, " is the largest")
if n2 > n1:
    if n2 > n3:
        print(n2, "is the largest")
if n3 > n1:
    if n3 > n2:
        print(n3, "is the largest")
