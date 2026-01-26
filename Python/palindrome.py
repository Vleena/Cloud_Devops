user = input("Enter a string: ")
reverse = user[::-1]
if user == reverse:
    print(user, "is palindrome")
else:
    print(user, "is not palindrome")