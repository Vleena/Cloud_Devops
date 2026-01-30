n= int(input("Enter number of series:"))
a= 0
b= 1
print(a)
print(b)
for i in range(2,n):
    sum=a+b
    print(sum)
    a=b
    b=sum

