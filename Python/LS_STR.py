user = input("Enter a list of string:").split()
target = input("Enter a string:")
for i in range(len(user)):
    if user[i] == target:
        print(user[i],"is found")
        break
else:
    print(target,"not found")