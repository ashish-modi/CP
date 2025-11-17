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
# Explanation:
# 1. We maintain a variable 'maximum' to keep track of the farthest index we can reach at any point.
# 2. We iterate through the array and update 'maximum' whenever we find a position that is reachable (i <= maximum).
# 3. When we reach the end of the current maximum reach, we increment the jump count and update the maximum reach to the farthest we can reach from the current positions.
# 4. We continue this process until we can reach or exceed the last index of the array.