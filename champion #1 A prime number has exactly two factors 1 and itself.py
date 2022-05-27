number = int(input("Enter a number :"))
factors = 0  # set the factor to zero at the beginneing
for divisible_number in range(number):
    divisible_number += 1  # divide the number by divisible number up to the number
    # get the remainder to know the number of factors
    remainder = number % divisible_number
    if remainder == 0:
        factors += 1  # if remainder is zero, then it is a factor of that number
if factors <= 2:  # A prime number has exactly two factors. therfore, if the number of factors is 2, then it is a prime number
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
