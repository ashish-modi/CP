# Leetcode Problem 347: Top K Frequent Elements
# Difficulty: Medium
# https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        dictionary = {}
        heap = []
        for i in range(length):
            if dictionary.get(nums[i], 0):
                dictionary[nums[i]] +=1
            else:
                dictionary[nums[i]] = 1
        # print("dictionary : ", dictionary)
        for key, value in dictionary.items():
            heapq.heappush(heap, [-value, key])
        result = deque()
        for i in range(k):
            val, ky = heapq.heappop(heap)
            result.append(ky)
        return list(result)
    
# Time Complexity : O(N log k) where N is the number of elements in the array
# Space Complexity : O(N) for the dictionary and heap  
# Explanation:
# 1. We use a dictionary to count the frequency of each element in the input array.
# 2. We then use a min-heap to keep track of the top k frequent elements.
# 3. We push the negative frequency and the element into the heap to simulate a max-heap.
# 4. Finally, we pop the top k elements from the heap and return them as the result. 
