

n1 = int(input("Enter number 1 :"))
n2 = int(input("Enter number 2 :"))
n3 = int(input("Enter number 3 :"))

if n1 < n2:
    if n1 < n3:
        print(n1, " is the smallest")
if n2 < n1:
    if n2 < n3:
        print(n2, "is the smallest")
if n3 < n1:
    if n3 < n2:
        print(n3, "is the smallest")
