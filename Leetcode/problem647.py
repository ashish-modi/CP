# Leetcode Problem 647: Palindromic Substrings
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
# Space Complexity: O(1)
# Note: This is a brute-force solution that checks all possible substrings of the input string `s` to determine if they are palindromic.
# Explanation:
# 1. We use two nested loops to generate all possible substrings of `s`.
# 2. For each substring, we check if it is equal to its reverse (i.e., if it is a palindrome).
# 3. If it is a palindrome, we increment the count.
# 4. Finally, we return the total count of palindromic substrings found in `s`. 