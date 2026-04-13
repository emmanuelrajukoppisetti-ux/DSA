#recursions
#Direct Recursion
'''def nums(n):
    if n==0:
        return
    print(n,end=" ")
    nums(n-1)
    
n=int(input("enter a number :"))
nums(n)'''

#Indirect Recursion
'''def funA(n):
    if n<=0:
        return
    print("A",n)
    funB(n-1)
def funB(n):
    if n<=0:
        return
    print("B",n)
    funA(n-1)
n=int(input("enter a number"))
funA(n)'''

#without using % check wether no is even or odd using recursion

'''def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
n=int(input("enter a number :"))
if is_even(n):
    print("even")
else:
    print("odd")'''

#nested recursion
def fun(n):
    if n>10:
        return n-1
    return fun(fun(n+2))
n=int(input("enter a number"))
print(fun(n))