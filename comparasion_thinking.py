'''n=int(input("enter no of elements"))
a=[]
for i in range (n) :
    ele=int(input("enter elements"))
    a.append(ele)
print("unsorted order is",a)
for i in range(n):
    for j in range(i,n-1):
        if a[i]<a[j+1]:
            a[i],a[j+1]=a[j+1],a[i]
print("sorted order",a)'''

#lambda function
'''n=int(input("enter no of elements"))
a=[]
for i in range (n):
    ele=int(input("enter element"))
    a.append(ele)
print("unsorted order:",a)
a.sort(key=lambda x : -x )
print("sorted array:",a)'''


#arrange strings according to their len in decending order
'''n=int(input("enter no of elements"))
a=[]
for i in range (n):
    ele=input("enter element")
    a.append(ele)
print("unsorted order:",a)
a.sort(key=lambda x : len(x),reverse=True)
print("sorted array:",a)'''

#add 2 to each alphabet in astring without ascii 


0


