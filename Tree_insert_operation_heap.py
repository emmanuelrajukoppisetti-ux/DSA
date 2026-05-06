'''#insert operation in a heap
import heapq
heap =[]
n=int(input("Enter number of nodes in the tree :"))
for i in range (n):
    val=int(input("Enter the value"))
    heapq.heappush(heap,val)
heapq.heapify(heap)
print("heap after insertion :",heap)'''


#Max element in a heap using insert operation in a heap
'''import heapq
heap =[]
n=int(input("Enter number of nodes in the tree :"))
for i in range (n):
    val=int(input("Enter the value"))
    heapq.heappush(heap,-val)
heapq.heapify(heap)
print(" Max heap internal value :",heap)
print("Max element removed ", -heapq.heappop(heap))
print("Heap after deletion ",[-x for x in heap])'''



#Sort the element in a heap using insert operation in a heap
import heapq
heap =[]
n=int(input("Enter number of nodes in the tree :"))
for i in range (n):
    val=int(input("Enter the value"))
    heapq.heappush(heap,val)
heapq.heapify(heap)
sorted_list=[]
while heap:
    sorted_list.append(heapq.heappop(heap))
print("Sorted element in the tree ",sorted_list)