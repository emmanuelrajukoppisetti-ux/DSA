n=int(input("enter the value of n"))
for i in range(n):
    for j in range(n):
        if j==n//2 or i==n//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    
    print()