#Delete from begin at DLL (doubly linled list):
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def delete_end(head):
    if head is None :
        return None
    temp=head
    if temp.next is None:
        return None
    while temp.next:
        temp=temp.next
    temp.prev.next=None
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
    new=node(val)
    new.next=head
    if head:
        head.prev=new
    head=new
display(head)
head=delete_end(head)
display(head)