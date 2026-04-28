def flip(arr,k):
    start=0
    while start<k:
        arr[start],arr[k]=arr[k],arr[start]
        start+=1
        k-=1
def pancake(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        max_index=0
    for i in range(n-1,0,-1):
        max_index=0
        for j in range(1,i+1):
            if arr[j]>arr[max_index]:
                max_index=j
        if max_index!=0:
            flip(arr,max_index)
        flip(arr,i)
    return arr

arr=list(map(int,input("enter elements").split()))
sortedarray=pancake(arr)
print("sorted array",sortedarray)


