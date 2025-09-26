class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        length = len(nums)
        window = length - k +1
        min_heap = []
        max_heap = []
        total = 0
        
        for i in range(length):
            heapq.heappush(max_heap, [-nums[i], i])
            heapq.heappush(min_heap, [nums[i],i])
        print("MaxHeap :", max_heap)
        print("MinHeap :", min_heap)
        m = k
        
        for i in range(length-k+1):
            maximum, max_index = heapq.heappop(max_heap)
            minimum, min_index = heapq.heappop(min_heap)
            maximum = -maximum
            elements = abs(max_index - min_index) + 1
            print("Elements : ", elements)
            take = min(length - elements + 1, m)
            # print("Maximum : ", maximum, "minimum : ", minimum, "take : ", take)
            total += (maximum - minimum)*take
            m-=take
            # if(m == 0):

        return total
            