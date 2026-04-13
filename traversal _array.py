'''traversal an array'''
arr=list(map(int,input("enter number :").split()))
for i in range(len(arr)):
    print(arr[i]+1,end="->")