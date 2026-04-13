"""searching an element and returning the index value"""
arr=list(map(int,input("Enter elements with space").split()))
search=int(input("enter the element to be seatched :"))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print("element found at index :",i)
        found=True
        break
if not found:
    print("element not found !!!")

#searching an word from given elements
'''arr=input("Enter elements with space :").split()
search=input("enter the word to be searched :")
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print("element found at index :",i)
        found=True
        break
if not found:
    print("element not found !!!")'''

#search elements greaterthan search element
'''arr=list(map(int,input("Enter elements with space").split()))
search=int(input("enter the element to be seatched :"))
found=False
for i in range (len(arr)):
    if arr[i]>search:
        print("elements greater than search is :",arr[i])
        found=True
if not found:
    print("element not found !!!")'''
