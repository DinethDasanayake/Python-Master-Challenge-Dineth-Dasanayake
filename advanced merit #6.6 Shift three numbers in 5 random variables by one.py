a = 2
b = 3
c = 4
d = 0
e = 0

print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)

temp = a
a = b
b = temp
temp = c
c = a
a = temp

a = e
e = temp
temp = b
b = d
d = temp

print("After shifting")
print("a =", a)
print("b =", b)
print("c =", c)
print("d =", d)
print("e =", e)
