# Problem: Maximum Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        maximum = -float(inf)
        summ = 0

        for i in range(length):
            summ += nums[i]
            maximum = max(summ, maximum)
        # ensure we reset summ if it goes negative so that we can start fresh from the next element
            if(summ < 0):
                summ = 0
        return maximum
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: This is Kadane's algorithm for finding the maximum subarray sum.