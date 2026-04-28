'''Rotate to the right by 1 an array'''
'''arr=list(map(int,input("Enter values").split()))
last=arr[-1]
for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
arr[0]=last
print("Rotated array",arr)'''

#move all zeros to the end of array
'''arr=list(map(int,input("enter values :").split()))
zero=0
for i in range(len(arr)):
    if arr[i] !=0:
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1
print("after moving zeros ",arr)'''


#move all zeros to start of array
'''arr=list(map(int,input("enter values :").split()))
zero=0
for i in range(len(arr)):
    if arr[i]==0:
        arr[zero],arr[i]=arr[i],arr[zero]
        zero+=1

































        
print("after moving zeros ",arr)'''


'''reverse sorted array'''
'''arr=list(map(int,input("Enter values :").split()))
start=0
end=len(arr)-1
while start<end:
    arr[start],arr[end]=arr[end],arr[start]
    start+=1
    end-=1
print("reverse array",arr)'''

#max subarray sum
'''arr=list(map(int,input("Enter values :").split()))
maxsum=arr[0]
current=arr[0]
for i in range(1,len(arr)):
    current=max(arr[i],current+arr[i])
    maxsum=max(maxsum,current)
print("max subarray sum :",maxsum)'''

 
