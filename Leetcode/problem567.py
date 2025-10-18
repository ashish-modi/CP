# Leetcode Problem 567: Permutation in String
# Difficulty: Medium
# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length1 = len(s1)
        length2 = len(s2)
        dictionary1 = {}
        for i in range(length1):
            dictionary1[s1[i]] = 1 + dictionary1.get(s1[i],0)
        for i in range(0,length2 - length1+1):
            dictionary2 = {}
            for j in range(i, i + length1):
                dictionary2[s2[j]] = 1 + dictionary2.get(s2[j], 0)
            if(dictionary1 == dictionary2):
                return True
        return False

# Time Complexity: O(N * M) where N is the length of s2 and M is the length of s1
# Space Complexity: O(1)
# Explanation: We use a sliding window approach to check each substring of s2 with the same length as s1.
# For each substring, we create a frequency dictionary and compare it with the frequency dictionary of s1.
# If they match, it means the substring is a permutation of s1, and we return True.
# If no such substring is found after checking all possibilities, we return False.