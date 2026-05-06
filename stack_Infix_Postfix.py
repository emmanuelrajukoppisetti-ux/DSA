#infix to postfix conversion.
'''
s = input("Enter the expression: ")
stack = []
result = ""
priority = {'+':1, '-':1, '*':2, '/':2}
for ch in s:
    if ch.isalnum():
        result += ch
    elif ch == '(':
        stack.append(ch)
    elif ch == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()  
    else:  
        while (stack and stack[-1] != '(' and 
               priority[ch] <= priority[stack[-1]]):
            result += stack.pop()
        stack.append(ch)
while stack:
    result += stack.pop()
print("Postfix:", result)

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