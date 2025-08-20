# Problem : Edit Distance
# Difficulty: Medium
# Link: https://leetcode.com/problems/edit-distance/

class Solution:
    def minD(self, word1, word2, dp, curr_index1, curr_index2, length1, length2):
        if(curr_index1 == length1):
            return length2 - (curr_index2 +1)
        if(curr_index2 == length2):
            return length1 - (curr_index1 +1)
        if(dp[curr_index1][curr_index2] != -1):
            return dp[curr_index1][curr_index2]
        inc = delete = upd = exc = float('inf')
        if(word1[curr_index1] != word2[curr_index2]):
            # Insert
            inc = 1 + self.minD(word1, word2, dp, curr_index1, curr_index2 + 1, length1, length2)
            # Delete
            delete = 1 + self.minD(word1, word2, dp, curr_index1 + 1, curr_index2, length1, length2)
            # update
            upd = 1 + self.minD(word1, word2, dp, curr_index1 + 1, curr_index2 + 1, length1, length2)
        else:
            exc = self.minD(word1, word2, dp, curr_index1 +1, curr_index2 + 1, length1 , length2)
        dp[curr_index1][curr_index2] = min(inc, delete, upd, exc)
        return dp[curr_index1][curr_index2]

    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)
        dp = [[-1]*(length2+1) for _ in range(length1 + 1)]
        return self.minD(word1, word2, dp, 0, 0,length1, length2) + 1
    
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Note: This is a recursive solution with memoization for calculating the minimum edit distance between two strings.    