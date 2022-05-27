import math
n = input("Enter the number :",)
sqrt = int(math.sqrt(int(n)))
if int(n)%sqrt==0:
    print(n, "is a square number.")
else:
    print(n, "is not a square number.")
