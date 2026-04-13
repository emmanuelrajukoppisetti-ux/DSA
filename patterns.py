#Pattern 1
'''
A 
A B 
A B C 
A B C D 
A B C D E 
'''
'''
n=5
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()    
'''

#Pattern 2
'''
A 
B B 
C C C 
D D D D 
E E E E E 
'''
'''
n=5
for i in range(n):
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()    
'''

#Pattern 3
'''
A A A A A 
B B B B 
C C C 
D D 
E 
'''
'''
n=5
for i in range(n):
    for j in range(n-i):
        print(chr(65+i),end=" ")
    print()            
'''

#Pattern 4
'''
A B C D E 
A B C D 
A B C 
A B 
A 
'''
'''
n=5
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()        
'''


#Pattern 5
'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''
'''
n=5
ch=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+ch),end=" ")
        ch+=1
    print()    
'''

#Pattern 6
''''
A 
B A 
C B A 
D C B A 
E D C B A 
'''
'''
n=5
for i in range(n):
    for j in range(i,-1,-1):
        print(chr(65+j),end=" ")
    print()    
'''