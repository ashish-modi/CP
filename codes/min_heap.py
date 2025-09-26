import heapq

# Create an empty heap
min_heap = []

# Push elements (heapify happens automatically)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 8)

print(min_heap)   # [2, 5, 8] (internally it's a binary heap, not sorted list)

# Pop smallest element
print(heapq.heappop(min_heap))  # 2
print(heapq.heappop(min_heap))  # 5
print(heapq.heappop(min_heap))  # 8
