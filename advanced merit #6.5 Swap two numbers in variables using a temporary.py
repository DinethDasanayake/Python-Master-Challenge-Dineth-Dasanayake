import random
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
print("Before swap")
print("Number 1 :", n1, ", Number 2 :", n2)
swap = n1
n1 = n2
n2 = swap

print("After swap")
print("Number 1 :", n1, ", Number :", n2)
