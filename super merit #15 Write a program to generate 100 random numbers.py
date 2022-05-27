import random
l=[]
for i in range(100):
    i = random.randint(0, 100)
    if i % 2 == 0 and i % 3 == 0:
        if i in l:
            pass
        else:
            l.append(i)
            print(i)
