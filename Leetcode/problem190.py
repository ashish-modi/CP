# Leetcode Problem 190: Reverse Bits
# Difficulty : Easy
# Link : https://leetcode.com/problems/reverse-bits/
# Based on Bit Manipulation

class Solution:
    def reverseBits(self, n: int) -> int:
        val = bin(n)[2:]
        rev = val[::-1]
        length = len(rev)
        return int(rev,2) * (1 << (32 - length))
        
# Time Complexity : O(log N) where N is the input number.
# Space Complexity : O(1) as we are using only constant space.
# Explanation:
# 1. We convert the input number to its binary representation using the bin function and remove