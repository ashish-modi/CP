# Leetcode Problem 213: House Robber II
# Difficulty: Medium
# URL: https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if(length == 1):
            return nums[0]
        if(length == 2):
            return max(nums[0], nums[1])
        dp1 = [0]*(length )
        dp2 = [0]*(length )
        
        i = 1
        dp1[0] = 0
        while(i > 0 and  i < length):  # 1st house is not included
            dp1[i] += nums[i] + max(dp1[i-2], dp1[i-3])
            i+=1
        i = 0
        while(i < length-1):  # last house is not included
            dp2[i] += nums[i] + max(dp2[i-2], dp2[i-3])
            i+=1
        return max(dp1[-1], dp1[-2], dp1[-3], dp2[-1], dp2[-2], dp2[-3])
    
# Time complexity: O(N) where N is the number of houses.
# Space complexity: O(N) for the dp arrays.
# Explanation: The solution uses dynamic programming to solve the problem in two scenarios:
# 1. Robbing houses from the second house to the last house (excluding the first house).
# 2. Robbing houses from the first house to the second-to-last house (excluding the last house).
# The maximum amount that can be robbed in both scenarios is calculated, and the overall maximum is returned as the result. 