# Leetcode Problem 53: Maximum Subarray
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
# Explanation:
# 1. We iterate through the array while maintaining a running sum of the current subarray.
# 2. If the running sum becomes negative, we reset it to zero since starting a new subarray from the next element could yield a higher sum.
# 3. We continuously update the maximum sum encountered during the iteration.