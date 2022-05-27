import random

n1 = random.randint(0, 10)
n2 = random.randint(0, 10)
n3 = random.randint(0, 10)

print("number 1=", n1)
print("number 2=", n2)
print("number 3=", n3)

print("Sum")
print(str(n1), "+", str(n2), "=", n1+n2)
print(str(n1), "+", str(n3), "=", n1+n3)
print(str(n2), "+", str(n3), "=", n2+n3)

print("Multiplication")
print(str(n1), "*", str(n2), "=", n1*n2)
print(str(n1), "*", str(n3), "=", n1*n3)
print(str(n2), "*", str(n3), "=", n2*n3)
