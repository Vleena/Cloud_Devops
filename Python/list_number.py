'''
input: 10 5 7 3
search: 7
Output: Found at index 2'''

user = list(map(int,input("Enter the list of integer:").split()))
search = int(input("search element:"))
for i in range(len(user)):
    if user[i]==search:
        print("Found at index",i)
        break
else:
    print(search,"not found")