#infix to postfix conversion
'''s=input("Enter infix expression :")
stack=[]
result=""
priority={'+':1,'-':1,'*':2,'/':2}
for ch in s:
    if ch.isalnum():
        result+=ch
    elif ch=='(':

'''


# postfix evaluation
s=input("Enter infix expression")
stack=[]
for ch in s:
    if ch.isdigit():
        stack.append(int(ch))
    else:
        b=stack.pop()
        a=stack.pop()
        if ch=='+': stack.append(a+b)
        elif ch=='-': stack.append(a-b)
        elif ch=='*': stack.append(a*b)
        elif ch=='/': stack.append(a//b)
print("Result",stack[0])