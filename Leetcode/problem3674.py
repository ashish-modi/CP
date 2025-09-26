# Leetcode Problem : Minimum Operations to equalize array
# Difficulty : Easy
# Link : https://leetcode.com/problems/minimum-operations-to-equalize-array/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length =len(nums)
        ele = nums[0]
        for i in range(length):
            if(nums[i] != ele):
                return 1
        return 0
    
# Time complexity : O(n)
# Space complexity : O(1)