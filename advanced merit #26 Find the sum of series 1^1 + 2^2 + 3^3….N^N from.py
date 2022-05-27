sum=0

n=int(input("Up to which number do you want the sum of square of that number :"))
for i in range(n):
    i+=1
    square=i**2
    sum+=square
    print(i,"^",i,"=",square)

print("Sum:",sum)
