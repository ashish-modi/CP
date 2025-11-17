# Leetcode Problem 152: Maximum Product Subarray
# Difficulty : Medium
# Link : https://leetcode.com/problems/maximum-product-subarray/
# Based on Two Pass Approach

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        maximum = -float('inf')
        prod = 1
        for i in range(length):
            prod *= nums[i]
            maximum = max(prod, maximum)
            if(prod == 0):
                prod = 1
        prod = 1
        for i in range(1,length+1):
            prod *= nums[-i]
            maximum = max(prod, maximum)
            if(prod == 0):
                prod = 1
        return maximum
    
# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(1) as we are using only constant space.
# Explanation:
# 1. We perform two passes through the array: one from left to right and another from right to left.
# 2. In each pass, we maintain a running product of the elements.
# 3. We update the maximum product found so far during each iteration.
# 4. If the running product becomes zero, we reset it to one to start a new product calculation.
# 5. Finally, we return the maximum product found during both passes.