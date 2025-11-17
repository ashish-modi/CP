# Leetcode Problem 268: Missing Number
# Difficulty : Easy
# Link : https://leetcode.com/problems/missing-number/
# Based on Bit Manipulation

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        val = res
        for i in range(res):
            val ^= i^nums[i]
        return val
    

# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(1) as we are using only constant space.

# Explanation:
# We use the property of XOR where a^a = 0 and a^0 = a.
# We initialize the result with n (length of array) and then XOR it with all indices and all numbers in the array. 
# The numbers that are present in the array will cancel out with their corresponding indices, leaving us with the missing number.
