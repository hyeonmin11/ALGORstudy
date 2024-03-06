import sys
import heapq

N = int(sys.stdin.readline())

lheap = []
rheap = []
ret = []

while(N):
    
    N -= 1
    
    num = int(sys.stdin.readline())
    
    if len(lheap) == len(rheap):
        heapq.heappush(lheap, (-num, num))
    else:
        heapq.heappush(rheap, (num, num))
    
    if rheap and lheap[0][1] > rheap[0][0]:
        min = heapq.heappop(rheap)[0]
        max = heapq.heappop(lheap)[1]
        
        heapq.heappush(lheap, (-min, min))
        heapq.heappush(rheap, (max, max))
    
    ret.append(lheap[0][1])

for j in ret:
    print(j)
    
    