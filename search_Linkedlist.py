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
def search(key):
    temp=head
    position=1
    while temp:
        if temp.data ==key:
            print("Element found in node",position)
            return
        temp=temp.next
        position+=1
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
key=int(input("enter value of the node to be search"))
search(key)
print("\n update linkedlist")
display()