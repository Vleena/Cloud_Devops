string = input("Enter a string:")
count=0
for i in string.lower():
    if i in ('a','e','i','o','u'):
        count=count+1
print(count)