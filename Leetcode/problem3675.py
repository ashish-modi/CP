# Leetcode problem : Minimum operations to transform string
# Difficulty : Medium
# Link : https://leetcode.com/problems/minimum-operations-to-transform-string/

class Solution:
    def minOperations(self, s: str) -> int:
        length =len(s)
        maximum = 0
        for i in range(length):
            ascii_char = ord(s[i])
            if(ascii_char != 97):
                val = 123 - ascii_char
                maximum = max(val, maximum)
        return maximum
    
# Time complexity : O(n)
# Space complexity : O(1)