# Leetcode Problem 45: Jump Game II
# Difficulty : Medium
# Link : https://leetcode.com/problems/jump-game-ii/
# Based on Greedy Algorithm

class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        maximum = nums[0]
        new_max = 0
        jump = 0
        for i in range(1,length):
            new_val = nums[i] + i
            if(new_val > new_max):
                new_max = new_val
            if(maximum >= length-1):
                jump+=1
                break
            if(i == maximum):
                jump+=1
                maximum = new_max

        return jump
    
# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(1) as we are using only constant space.
