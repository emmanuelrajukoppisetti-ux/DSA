import math
arr = list(map(int,input("Enter elements:").split()))
target=int(input("Enter element to be searched:"))
n=len(arr)
step=int(math.sqrt(n))
i=0
while i<n and arr[min(i+step , n)-1]<target:
    i+=step
for j in range(i,min(i+step,n)):
    if arr[j]==target:
        print("found at index :",i)
        break
else:
    print("not found !!!!")