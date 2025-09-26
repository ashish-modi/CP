# Leetcode Problem 55: Jump Game
# Difficulty : Medium
# Link : https://leetcode.com/problems/jump-game/
# Based on Greedy Algorithm

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        maximum = nums[0]
        for i in range(1,length):
            if(i <= maximum):
                new_max = i + nums[i]
                maximum = max(maximum, new_max)
            else:
                return False
        return True
    
# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(1) as we are using only constant space.