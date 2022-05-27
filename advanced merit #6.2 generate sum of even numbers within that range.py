n1 = input("Enter number 1:")
n2 = input("Enter number 2:")

if n1 > n2:
    big = int(n1)
    small = int(n2)
else:
    big = int(n2)
    small = int(n1)

range_n = small
sum = 0

print("Even numbers between", small, "and", big)
even_n = 0
while range_n < big:
    range_n += 1
    mod = range_n % 2
    if mod == 0:
        even_n = range_n
        print(even_n)
        sum += even_n

print("Sum =", sum)
