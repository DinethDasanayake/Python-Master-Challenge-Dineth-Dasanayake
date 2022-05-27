import random
l = []
n=[]
large=100
for i in range(100):
    i = random.randint(0, 100)
    if i % 2 == 0 and i % 3 == 0 and i % 10==0:
        if i in l:
            pass
        else:
            l.append(i)
            n.append(i)
n.sort()
print(n)

        
