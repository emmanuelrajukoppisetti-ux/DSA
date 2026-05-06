'''num=int(input("enter a number"))
fact=1
i=1  
while i<=num:
    fact*=i
    i+=1
print(fact)'''

n=int(input("enter value :"))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)