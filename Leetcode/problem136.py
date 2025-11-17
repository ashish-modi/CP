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
# Explanation:
# 1. We use the reduce function from the functools module to apply the XOR operation across all elements in the input array.
# 2. The XOR operation has the property that a^a = 0 and a^0 = a, which means that pairs of identical numbers will cancel each other out.
# 3. As a result, after applying the XOR operation to all elements, only the unique number that appears once will remain.
# 4. We return this unique number as the result.