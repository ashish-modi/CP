# Leetcode Problem 7: Reverse Integer
# Difficulty : Medium
# Link : https://leetcode.com/problems/reverse-integer/
# Based on Math and String Manipulation

class Solution:
    def reverse(self, x: int) -> int:
        tmp = abs(x)
        rev = int(str(tmp)[::-1])
        if( x < 0):
            rev *= -1
        return 0 if (rev <= -(2**31)) or (rev > (2**31 -1)) else rev
        
# Time complexity : O(log N) where N is the input number.
# Space complexity : O(1) as we are using only constant space.