# Problem: Maximum Product Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        maximum = -float('inf')
        prod = 1

        # Forward pass for prefix product 
        for i in range(length):
            prod *= nums[i]
            maximum = max(prod, maximum)
            # Reset product if it becomes zero to avoid multiplying by zero in the next iteration
            if(prod == 0):
                prod = 1
        prod = 1
        # Backward pass for suffix product
        for i in range(1,length+1):
            prod *= nums[-i]
            maximum = max(prod, maximum)
            # Reset product if it becomes zero to avoid multiplying by zero in the next iteration
            if(prod == 0):
                prod = 1
        return maximum
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# Note: This is a variation of Kadane's algorithm for finding the maximum product subarray.