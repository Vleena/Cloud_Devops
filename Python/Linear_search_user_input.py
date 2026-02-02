arr = list(map(int,input("Enter a integer list:").split()))
target = int(input("Enter a searching number:"))

for i in arr:
    if i==target:
        print(i,"element found")
        break
if i!=target:
    print(target,"elemenis not found")
