#write a progran to reverse a given number
n=int(input("enter a number"))
while n!=0:
    r=n%10
    print(r,end='')
    n=n//10