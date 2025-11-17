# Leetcode Problem 3674: Minimum Operations to equalize array
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
# Explanation :
# We check if all elements in the array are equal.
# If they are equal, we return 0 as no operations are needed.
# If they are not equal, we return 1 as we can make all elements equal in one operation by changing all elements to the value of any one element.