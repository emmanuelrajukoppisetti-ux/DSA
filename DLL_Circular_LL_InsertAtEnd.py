class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
def insert_end(head,data):
    new=node(data)
    if head is None:
        new.next=new
        return new
    temp=head
    while temp.next !=head:
        temp=temp.next
    temp.next=head
    return head
def display(head):
    if head is None:
        return
    temp=head
    while True:
        print(temp.data,end="->")
        temp=temp.next
        if temp==head:
            print(temp.data)
            break
head=None
n=int(input("enter number of nodes"))
for _ in range(n):
    val=int(input("enter value :"))
    head=insert_end(head,val)
display(head)