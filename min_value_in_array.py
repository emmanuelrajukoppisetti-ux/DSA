'''program to find the minimum value in a user defined array '''
 
arr=list(map(int,input("enter the number").split()))
min_value=arr[0]
for i in arr:
    if i<min_value:
        min_value=i
print(min_value)