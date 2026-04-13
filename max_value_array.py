'''program to find the maximum value in a user defined array '''
 
arr=list(map(int,input("enter the number").split()))
max_value=arr[0]
for i in arr:
    if i>max_value:
        max_value=i
print(max_value)