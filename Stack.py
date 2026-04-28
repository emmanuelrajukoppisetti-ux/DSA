#stack Operations
'''
stack =[]

#push
stack.append(11)
stack.append(22)
stack.append(33)

print(stack)

#pop
stack.pop()
print(stack)
stack.pop()
print(stack)
#peek
print(stack[-1])
#size
print(len(stack))
print(len(stack)==0)
'''
'''stack=[]
size=2
if len(stack)<size:
    stack.append(10)
else:
    print("stack overflow")
if len(stack)<size:
    stack.append(16)
else:
    print("stack overflow")
print(stack)'''

'''
def three():
    print("this is inside function-3")
def two():
    print("this is inside function-2")
    three()
def one():
    print("this is inside function-1")
    two()
one()'''

def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
n=int(input("enter number"))
count(n)