# Leetcode Problem 136: Single Number
# Difficulty : Easy
# Link : https://leetcode.com/problems/single-number/
# Based on Bit Manipulation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = reduce(lambda a,b: b^a, nums)
        return(res)
    
# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(1) as we are using only constant space.