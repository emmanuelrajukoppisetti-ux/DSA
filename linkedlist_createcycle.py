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
#testing(create cycle)
def createcycle(pos):
    global head
    if pos == -1:
        cyclenode=temp
        


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