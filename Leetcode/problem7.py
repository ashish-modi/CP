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
# Explanation:
# 1. We convert the absolute value of the integer to a string and reverse it.
# 2. We then convert the reversed string back to an integer.
# 3. If the original integer was negative, we negate the reversed integer.
# 4. Finally, we check if the reversed integer is within the 32-bit signed integer range. If it is not, we return 0; otherwise, we return the reversed integer.