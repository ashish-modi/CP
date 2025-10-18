# Leetcode Problem 424: Longest Repeating Character Replacement
# Difficulty: Medium
# https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        left = right = 0
        maximum = 0
        dictionary = {}
        res = 0
        for right in range(length):
            dictionary[s[right]] = 1 + dictionary.get(s[right],0)
            maximum = max(maximum, dictionary[s[right]])
            while (right - left + 1) - maximum > k:
                dictionary[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
    
# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: We use a sliding window approach to find the longest substring that can be transformed into a string with all identical characters by replacing at most k characters.
# We maintain a count of the most frequent character in the current window and adjust the window size accordingly.
# The dictionary keeps track of character frequencies, and we update the maximum frequency as we expand the window. If the number of characters that need to be replaced exceeds k, we shrink the window from the left.
# The result is updated with the maximum length of valid windows found during the process.
