# Leetcode problem 2486: Append characters to string to make Subsequence
# Difficulty : Medium
# Url : https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        length1 = len(s)
        length2 = len(t)
        j = 0
        for i in range(length1):
            if(j < length2 and s[i] == t[j]):
                j +=1
        
        return length2 - j
    
# Time complexity : O(n), where n is the length of string s.
# Space complexity : O(1)
# Explanation : We can use two pointers to check if t is a subsequence of s.
# We start with the first character of t and check if it is present in s. 
# If it is, we move to the next character of t and continue this process until we have checked all characters of t.
# If we have checked all characters of t, then we return the number of characters that we need to append to s to make t a subsequence of s, 
# which is the length of t minus the number of characters of t that we have found in s.