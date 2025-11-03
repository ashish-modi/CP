# Leetcode Problem 10: Regular Expression Matching
# Difficulty: Hard
# URL: https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = list(s)
        p = list(p)
        length1 = len(s)
        length2 = len(p)
        dp = [[-1]*(length2+1) for _ in range(length1+1)]
        def matched(idx1, idx2):
            if(idx1 >= length1 and idx2 >= length2):
                return True
            if(idx2 >= length2):
                return False
            if(dp[idx1][idx2] != -1):
                return dp[idx1][idx2]
            match = idx1 < length1 and (s[idx1] == p[idx2] or p[idx2] == '.')
            
            if(idx2 + 1 < length2 and p[idx2+1] == "*"):
                dp[idx1][idx2] = matched(idx1, idx2+2) or (match and matched(idx1+1, idx2))
                return dp[idx1][idx2]
            
            if match:
                dp[idx1][idx2] = matched(idx1+1, idx2+1)
                return dp[idx1][idx2]
            dp[idx1][idx2] = False
            return dp[idx1][idx2]

            
        return matched(0,0)

# Time complexity: O(M*N) where M is the length of string s and N is the length of pattern p.
# Space complexity: O(M*N) for the dp table used to store intermediate results.
# Explanation: The solution uses dynamic programming with memoization to determine if the string s matches the pattern p.
# It defines a recursive function matched(idx1, idx2) that checks if the substring of s starting from idx1 matches the substring of p starting from idx2.
# The function handles different cases based on whether the current characters match, and whether the next character in p is a '*'.
# The results are stored in a dp table to avoid redundant calculations, leading to an overall time complexity of O(M*N).