# LeetCode Problem 295: Find Median from Data Stream
# Difficulty: Hard
# URL: https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        self.s_heap_size = 0
        self.l_heap_size = 0

    def addNum(self, num: int) -> None:
        if not self.small_heap and not self.large_heap:
            heapq.heappush(self.small_heap, -num)
            self.s_heap_size += 1
            return

        if(self.s_heap_size < self.l_heap_size): # insert into small heap
            if(self.large_heap and num <= self.large_heap[0]):
                heapq.heappush(self.small_heap, -num)
            else:
                ele = heapq.heappop(self.large_heap)
                heapq.heappush(self.small_heap,-ele)
                heapq.heappush(self.large_heap, num)
            self.s_heap_size +=1
        else:
            if(self.small_heap and num >= -self.small_heap[0]):
                heapq.heappush(self.large_heap, num)
            else:
                ele = -heapq.heappop(self.small_heap)
                heapq.heappush(self.large_heap,ele)
                heapq.heappush(self.small_heap, -num)

            self.l_heap_size +=1


    def findMedian(self) -> float:
        if(self.s_heap_size > self.l_heap_size):
            return -self.small_heap[0]
        elif(self.l_heap_size > self.s_heap_size):
            return self.large_heap[0]
        else:
            return (-self.small_heap[0] + self.large_heap[0])/2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Time complexity:
# addNum: O(log N) - Inserting a number into one of the heaps takes logarithmic time.
# findMedian: O(1) - Finding the median takes constant time since it involves just accessing the top elements of the heaps.
# Space complexity:
# O(N) - In the worst case, we may store all numbers in the two heaps.
# Explanation:
# The MedianFinder class uses two heaps (a max-heap for the lower half of numbers and a min-heap for the upper half) to efficiently maintain and retrieve the median of a stream of numbers.