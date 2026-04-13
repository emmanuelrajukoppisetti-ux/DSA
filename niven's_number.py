num=int (input("enter a number"))
temp=num
s=0

while temp!=0:
    r=temp%10
    s+=r
    temp//=10
if num%s==0:
    print(num,"is an nivens number")
else:
    print(num,"is not an nivens number")