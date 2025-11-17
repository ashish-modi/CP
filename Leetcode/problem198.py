# Leetcode Problem 198: House Robber
# Difficulty: Medium
# Link: https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(2, length):
            if(i== 2):
                nums[i] += nums[i - 2]
            else:
                nums[i] += max(nums[i-2], nums[i-3])
        if(length == 1):
            return nums[-1]
        if(length == 2):
            return max(nums[-1], nums[-2])
        else:
            return max(nums[-1], nums[-2], nums[-3])
        
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: This is a dynamic programming solution to find the maximum amount of money that can be robbed without alerting the police, given that adjacent houses cannot be robbed on the same night.
# Explanation:
# 1. We iterate through the list of house values starting from the third house.
# 2. For each house, we update its value to be the sum of its original value and the maximum value that can be robbed from the houses before the adjacent one.
# 3. Finally, we return the maximum value from the last three houses, as they represent the maximum amount that can be robbed without alerting the police.