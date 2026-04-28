class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def search(head,key):
    temp=head
    pos=1
    while temp:
        if temp.data==key:
            return pos
        temp=temp.next
        pos+=1
    return -1
head=None
n=int(input("enter number of nodes"))
for _ in range(n):
    val=int(input("enter value :"))
    if head is None:
        head=node(val)
    else:
        temp=head
        while temp.next:
            temp=temp.next
        new=node(val)
        temp.next=new
        new.prev=temp
key=int(input("enter the value you wanna deleta: "))
pos=search(head,key)
if pos!=-1:
    print(key,"found at node",pos)
else:
    print("Not found...!!")
