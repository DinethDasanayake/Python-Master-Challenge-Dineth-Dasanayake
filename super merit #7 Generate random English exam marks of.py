#7
import random
sum = 0
s = 0
for i in range(10):
    i = random.randint(0, 100)
    s += 1
    sum += i
    print(s, "th student :", i)
    
average = sum/10
print("Average =", average)

