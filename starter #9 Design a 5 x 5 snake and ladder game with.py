import random

total = 25

s1_start = 12
s1_end = 3
s2_start = 21
s2_end = 9

l1_start = 5
l1_end = 14
l2_start = 10
l2_end = 23

val = 0
p = 0

print("total number of squares",total)
while val == 1 or 6:
    val = random.randint(1, 6)
    p += val
    while p < 25:
        val = random.randint(1, 6)
        p += val
        print("value=", val)
        print("player's place=", p)
        if p == s1_start:
            p = s1_end
            print("player=", p)
        elif p == s2_start:
            p = s2_end
            print("player=", p)
        elif p == l1_start:
            p = l1_end
            print("player=", p)
        elif p == l2_start:
            p = l2_end
            print("player=", p)
        else:
            pass
