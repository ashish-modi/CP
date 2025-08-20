# Leetcode Problem: Palindromic Substrings
# Difficulty: Medium
# Link: https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        length = len(s)
        count = 0
        for i in range(length):
            for j in range(i, length):
                wrd = s[i:j+1]
                if(wrd == wrd[::-1]):
                    count +=1
        return count
    
# Time Complexity: O(n^3) 