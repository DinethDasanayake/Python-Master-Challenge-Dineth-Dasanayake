import random


# comp = number generated by the computer
n = 0
comp = random.randint(0, 100)
while comp != n:
    n = int(input("Enter a random number between 1 and 100 :"))
    comp = random.randint(0, 100)
    print("Number generated by the computer :", comp)
print("YOU WON")
