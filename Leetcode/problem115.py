# Leetcode Problem: Distinct Subsequences
# Difficulty: Hard
# Link: https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        length1 = len(s)
        length2 = len(t)
        dp = [[-1] * (1001) for _ in range(1001)]
        def count(idx1, idx2):
            if(idx1 == length1 and idx2 == length2):
                return 1
            if(idx1 > length1 or idx2 > length2):
                return 0
            if(dp[idx1][idx2] != -1):
                return dp[idx1][idx2]
            include = exclude = 0
            if(idx1 < length1 and idx2 < length2 and s[idx1] == t[idx2]):
                include = count(idx1 +1, idx2 + 1)
            exclude = count(idx1 + 1, idx2)
            dp[idx1][idx2] =  exclude + include
            return dp[idx1][idx2]

        return count(0,0)
    
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Note: This is a recursive solution with memoization to count the number of distinct subsequences of string `s` that equal string `t`.
# The solution uses dynamic programming to store intermediate results in a 2D array `dp`, where `dp[i][j]` represents the number of distinct subsequences of the first `i` characters of `s` that equal the first `j` characters of `t`.
# The function `count` recursively explores both including and excluding the current character of `s`, updating the `dp` array to avoid redundant calculations.
# The base case checks if both indices have reached the end of their respective strings, returning 1 if true and 0 if either index exceeds the string length.
# The function returns the total count of distinct subsequences that match `t` from `s`.