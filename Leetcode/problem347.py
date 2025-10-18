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
