# Leetcode Problem: Interleaving String
# Difficulty: Medium
# Link: https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
         length1 = len(s1)
         length2 = len(s2)
         length3 = len(s3)
         dp = [[-1]*(200) for _ in range(200)]
         def possible(idx_s1, idx_s2, idx_s3):
            if(idx_s1 == length1 and idx_s2 == length2 and idx_s3 == length3):
                return True
            m1 = False
            m2 = False
            if(dp[idx_s1][idx_s2] != -1):
                return dp[idx_s1][idx_s2]
            if(idx_s1 < length1 and idx_s3 < length3 and s1[idx_s1] == s3[idx_s3]):
                m1 = possible(idx_s1+1, idx_s2, idx_s3+1)
            if(idx_s2 < length2 and idx_s3 < length3 and s2[idx_s2] == s3[idx_s3]):
                m2 = possible(idx_s1, idx_s2+1, idx_s3+1)
            dp[idx_s1][idx_s2] =  m1 or m2
            return dp[idx_s1][idx_s2]

         return possible(0,0,0)
    
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Note: This is a recursive solution with memoization to determine if a string `s3` is an interleaving of two other strings `s1` and `s2`.
# The solution uses dynamic programming to store intermediate results in a 2D array `dp`, where `dp[i][j]` represents whether the first `i` characters of `s1` and the first `j` characters of `s2` can form the first `i + j` characters of `s3`.
# The function `possible` recursively checks both possibilities of taking a character from `s1` or `s2` and updates the `dp` array to avoid redundant calculations.