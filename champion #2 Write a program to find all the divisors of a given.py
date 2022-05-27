number = int(input("Enter a number up to 1000 :"))

if number<=1000:
    print("Divisors of", number)

    for divisible_number in range(number):
        divisible_number += 1
        remainder = number % divisible_number
        if remainder == 0:
            divisor = number / divisible_number
            print(int(divisor))
else:
    print("please enter a vaild number")