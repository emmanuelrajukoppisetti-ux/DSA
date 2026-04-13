'''linear search'''
arr=list(map(int,input("enter elements : ").split()))
target=int(input("enter element to be searched"))
found=False
for i in range(len(arr)):
    if arr[i]==target:
        print("element is found at index :",i)
        found=True
        break
if not found:
    print("element is not found !!!!") 