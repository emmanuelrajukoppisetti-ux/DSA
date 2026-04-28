class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
def insert(data):
    global head
    newnode=node(data)
    newnode.next=head
    head=newnode
def reverse():
    global head
    prev=None
    curr=head
    while curr:
        nextnode=curr.next
        curr.next=prev
        prev=curr
        curr=nextnode
    head=prev
    print("Reversed linkedlist :")


def display():
    temp=head
    while temp:
        print(temp.data,end="->")
        temp=temp.next
    print("None")

n=int(input("Enter number of nodes:"))    
for _ in range(n):
    val=int(input("enter value:"))
    insert(val)
print("Inserted Linkedlist")
display()
reverse()
print("\n update linkedlist")
display()
