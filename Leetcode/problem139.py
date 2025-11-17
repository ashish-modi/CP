# Leetcode Problem 139: Word Break
# Difficulty: Medium
# Link: https://leetcode.com/problems/word-break/

class Solution:
    def breakable(self, s, dp, last_included, curr_index, length, dictionary):
        n = s[last_included + 1: curr_index + 1]
        if(curr_index == length -1):
            return True if(dictionary.get(n,0)) else False
        
        if(dp[last_included][curr_index] != -1):
            return dp[last_included][curr_index]
        # include 
        include = False
        if(dictionary.get(n,0)):
            include = self.breakable(s, dp, curr_index, curr_index + 1, length, dictionary)
        # exclude
        exclude = self.breakable(s, dp, last_included, curr_index + 1, length, dictionary)
        dp[last_included][curr_index] = include or exclude
        return dp[last_included][curr_index]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dictionary = {}
        for word in wordDict:
            dictionary[word] = 1
        dp = [[-1] *(length + 1) for _ in range(length+1)]
        return self.breakable(s, dp, -1, 0, length, dictionary)
    
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Note: This is a recursive solution with memoization to determine if a string can be segmented into words from a given dictionary.
# Explanation:
# 1. We define a recursive function `breakable` that checks if the substring from the last included index to the current index can form valid words.
# 2. The base case checks if we have reached the end of the string and whether the last substring is in the dictionary.