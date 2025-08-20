# Leetcode Problem: Decode Ways
# Difficulty: Medium
# Link: https://leetcode.com/problems/decode-ways/

class Solution:
    def count(self, s, dp, last_included, curr_index, length):
        n = int(s[last_included+1:curr_index+1])
        if(curr_index == length-1):
            return 1 if(n >=1 and n <=26) else 0

        if(n < 1 or n > 26):
            return 0
        # include
        if(dp[last_included][curr_index] != -1):
            return dp[last_included][curr_index]
        include = self.count(s, dp, curr_index, curr_index + 1, length)

        exclude = self.count(s, dp, last_included, curr_index + 1, length)
    
        dp[last_included][curr_index] = include + exclude
        return dp[last_included][curr_index]


    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = [[-1]*(length+1) for _ in range(length+1)]
        return self.count(s, dp, -1, 0,length)
    
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Note: This is a recursive solution with memoization to count the number of ways to decode a string of digits into letters, where '1' maps to 'A', '2' to 'B', ..., and '26' to 'Z'.