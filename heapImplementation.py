from heapq import heapify, heappush, heappop

size=int(input('Enter the size:'))
heap=[]

for i in range(0,size):
    item=int(input('Enter the item:'))
    heappush(heap,item)

print(heap)
heapify(heap)
print('After heapifying...') # Heapifying process
print(heap)

print(heappop(heap),'is popped')
print(heap)