# Leetcode Problem 371: Sum of Two Integers
# Difficulty: Medium
# URL: https://leetcode.com/problems/sum-of-two-integers/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        a &= MASK
        b &= MASK

        
        while(b):
            ans = (a ^ b) & MASK          
            carry = ((a & b) << 1) & MASK 
            a, b = ans, carry
        
        return a if a <= MAX_INT else ~(a ^ MASK)

                
# Time complexity: O(1) since the number of bits in an integer is fixed (32 bits).
# Space complexity: O(1) as we are using a constant amount of space.
# Explanation: The solution uses bitwise operations to calculate the sum of two integers without using the '+' operator.
# It repeatedly calculates the sum without carry (using XOR) and the carry itself (using AND and left shift) until there are no more carries left.
# The result is adjusted for negative numbers using a mask to ensure it fits within the 32-bit signed integer range.