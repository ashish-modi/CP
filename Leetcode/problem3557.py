# Leetcode problem 3557: Maximum Number of Non-Overlapping Substrings
# Difficulty: Medium
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

class Solution:
    def maxSubstrings(self, word: str) -> int:
        length = len(word)
        dictionary = {}
        count = {}
        prev = -1
        total = 0
        for i in range(length):
            if(dictionary.get(word[i],0)):
                prev_pos = dictionary[word[i]] -1
                if(count[word[i]] == 1):
                    if(prev_pos > prev and (i- prev_pos+1) >=4):
                        count[word[i]] = 0
                        prev = i
                        total +=1
                else:
                    count[word[i]] = 1
                if(prev_pos <= prev):
                    dictionary[word[i]] = i+1
            else:
                dictionary[word[i]] = i+1
                count[word[i]] = 1
        return total
    
# Time complexity: O(n) where n is the length of the string word
# Space complexity: O(1) as the dictionary can have at most 26 characters
# Explanation:
# The function calculates the maximum number of non-overlapping substrings in the input string word.
# It uses a dictionary to track the last occurrence of each character and a count dictionary
# to track if a character has been counted in the current substring. The function iterates
# through the string and updates the counts and positions accordingly to find valid substrings.