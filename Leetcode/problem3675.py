# Leetcode problem 3675: Minimum operations to transform string
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
# Explanation :
# We iterate through the string and for each character, we calculate the number of operations needed to transform it to 'a'.
# The number of operations needed is given by 123 - ASCII value of the character.
# We keep track of the maximum number of operations needed among all characters and return it as the result.