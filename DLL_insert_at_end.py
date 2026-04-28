#insert at End at DLL (doubly linled):
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insert_end(head,data):
    newnode=node(data)
    if head is None:
        return newnode
    temp=head
    while temp.next:
        temp=temp.next
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
    head=insert_end(head,val)
display(head)