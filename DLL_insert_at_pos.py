#insert at End at DLL (doubly linled list):
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insert_pos(head,data,pos):
    newnode=node(data)
    if pos==1:
        if head:
            head.prev=newnode
            newnode.next=head
        return newnode
    temp=head
    for _ in range(pos-2):
        temp=temp.next
    newnode.next=temp.next
    if temp.next:
        temp.next.prev=newnode
    temp.next=newnode    
    newnode.prev=temp
    return head
        
def display(head):
    temp=head
    while temp:
        print(temp.data,end="<->")
        temp=temp.next
    print("None")
head=None
n=int(input("enter number of nodes : "))
for _ in range(n):
    val=int(input("Enter value :"))
    head=insert_pos(head,val,_+1)
pos=int(input("enter position to insert : "))
val=int(input("enter value : "))
head=insert_pos(head,val,pos)
display(head)