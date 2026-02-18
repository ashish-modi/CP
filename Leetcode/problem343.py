# LeetCode Problem 343: Integer Break
# Difficulty: Medium
# URL: https://leetcode.com/problems/integer-break/

class Solution:
    

    def integerBreak(self, n: int) -> int:
        states = {1:1}

        def maximum_product(num: int) -> int:
            if(num ==1):
                return 1
            if(num in states):
                return states[num]
            maximum = 0 if num == n else num
            for i in range(1,num):
                maximum = max(maximum_product(i)* maximum_product(num-i), maximum)
            states[num] = maximum
            return maximum

        return maximum_product(n)
    
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Explanation:
# The function integerBreak uses a helper function maximum_product to compute the maximum product
# obtainable by breaking the integer n into at least two positive integers. It employs memoization to
# store previously computed results in the states dictionary, which helps to avoid redundant calculations.
# The maximum_product function recursively explores all possible ways to split the integer and calculates
# the maximum product for each split. The base case is when the number is 1, which returns 1. The final result is obtained by calling maximum_product with the input n.
