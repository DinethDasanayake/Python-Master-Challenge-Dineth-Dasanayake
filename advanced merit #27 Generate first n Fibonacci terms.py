inp = input("Enter the fibonacci term you want :",)
inp = int(inp)


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


while inp < 100:
    inp += 1
    print(inp, "th term :", fib(inp))
