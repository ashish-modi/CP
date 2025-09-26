# Max Heap implementation using heapq by inverting values
# Trick : Push negative values to simulate max-heap behavior

import heapq

max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -8)

print(-heapq.heappop(max_heap))  # 8
print(-heapq.heappop(max_heap))  # 5
print(-heapq.heappop(max_heap))  # 2
