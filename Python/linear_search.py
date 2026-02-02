a= [10,20,30,40]
target =0
for i in range(len(a)):
    if a[i]==target:
        print("Element found in a index",i)
        break
if a[i]!=target:
    print("element not found")