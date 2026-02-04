def binary_search(user,target):
    user.sort()
    low = 0
    high = len(user)-1
    while low<=high:
        mid =(low + high)//2
        if user[mid]==target:
            return mid
        elif user[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

user = list(map(int,input("Enter the list:").split()))
target = int(input("Enter a target number:"))
result= binary_search(user,target)

if result !=-1:
    print(target,"element found in the index",result)
else:
    print(target,"element not found")