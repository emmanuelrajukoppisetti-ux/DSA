#operations
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
def delete(value):
    global head
    temp=head
    if temp and temp.data ==value:
        head=temp.next
        return
    prev=None 
    while temp and temp.data!=value:
        prev=temp   
        temp=temp.next
    if temp is None:
        print('value not in linkedlist....') 
        return
    prev.next=temp.next
    print("Deleted value :",value)
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
key=int(input("enter value of the node to be deleted"))
delete(key)
print("\n update linkedlist")
display() 