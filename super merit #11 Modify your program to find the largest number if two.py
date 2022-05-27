import random

n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2 :"))
n3 = int(input("Enter number 3 :"))

if n1 > n2:
    if n1 > n3:
        print(n1, " is the largest")
    elif n1 == n3:
        print("n1 and n3 are equal")
    elif n3>n1:
        print("n3 is the largest")
    else:
        pass
elif n2 > n1:
    if n2 > n3:
        print(n2, "is the largest")
    elif n2 == n3:
        print("n2 and n3 are equal")
    elif n3>n2:
        print("n3 is largest")
    else:
        pass  
elif n3 > n2:
    if n3 > n1:
        print(n3, "is the largest")
    elif n3 == n1:
        print("n3 and n1 are equal")
    else:
        pass
elif n1==n2:
    if n1>n3:
        print("n1 and n2 are equal")
    else:
        pass
elif n3>n1:
        print("n3 is the largest")
else:
    pass