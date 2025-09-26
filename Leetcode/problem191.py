# Leetcode Problem 191: Number of 1 Bits
# Difficulty : Easy
# Link : https://leetcode.com/problems/number-of-1-bits/
# Based on Bit Manipulation

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n>0):
            if(n%2 == 1):
                count +=1
            n//=2
        return count
            
# Time Complexity : O(log N) where N is the input number.
# Space Complexity : O(1) as we are using only constant space.  