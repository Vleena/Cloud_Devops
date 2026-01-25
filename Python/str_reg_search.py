import re

string = input("Enter a string:")
pattern = r"quick"

search = re.search(pattern,string)
if search:
    print(pattern, "present in a string")
else:
    print(pattern, "is not present in a string")