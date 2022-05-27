n1 = input("Enter number 1:")
n2 = input("Enter number 2:")

if n1 > n2:
    big = int(n1)
    small = int(n2)
else:
    big = int(n2)
    small = int(n1)

range_n = small
print(range_n)
sum = 0

print("Odd numbers between",small,"and",big)
odd_n = 0
while range_n < big:
    range_n += 1
    mod = range_n % 2
    if mod == 1:
        odd_n = range_n
        print(odd_n)
        sum += odd_n

print("Sum =",sum)
