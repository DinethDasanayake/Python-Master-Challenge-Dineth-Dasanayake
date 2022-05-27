'''n1 = input("Enter number 1:")
n2 = input("Enter number 2:")

if n1 > n2:
    big = int(n1)
    small = int(n2)
else:
    big = int(n2)
    small = int(n1)

range_n = small
print(small)

print("Traingular numbers between", small, "and", big)
'''
# Python3 program to check if a number is a
# triangular number using simple approach.

# Returns True if 'num' is triangular, else False
def isTriangular(num):
    # A Triangular number must be
	# sum of first n natural numbers
	sum, n = 0, 1

	while(sum <= num):
	
		sum = sum + n
		if (sum == num):
			return True
		n += 1

	return False

# Driver code
n = 55
if (isTriangular(n)):
	print("The number is a triangular number")
else:
	print("The number is NOT a triangular number")

# This code is contributed by Smitha Dinesh Semwal.

