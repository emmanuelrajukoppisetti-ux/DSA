num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    r=temp%10
    fact = 1
    i=1
    while i<=r:
        fact*=i
        i+=1
        sum+=fact
        temp//=10
if sum==num:
    print("strong number")
else:
    print("not")