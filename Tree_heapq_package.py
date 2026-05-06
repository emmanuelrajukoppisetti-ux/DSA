#heap push
'''import heapq
heap=[]
heapq.heappush(heap,5)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappushpop(heap,7))
print(heap)'''



import heapq
heap=[]
heapq.heappush(heap,5)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heapify(heap)
print(heap)
print(heapq.heapreplace(heap,8))
print(heap)
print(heapq.nlargest(1,heap))
print(heapq.nsmallest(1,heap))