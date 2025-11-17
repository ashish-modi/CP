# Leetcode Problem 3: Longest Substring Without Repeating Characters
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        pos = {}
        right = maximum = left = 0
        
        while(right < length):
            if(pos.get(s[right], 0)):
                if(left < pos[s[right]]):
                    left = pos[s[right]]
                pos[s[right]] = right + 1
            else:
                pos[s[right]] = right +1
            maximum = max(maximum, right - left+1)
            right +=1
        return maximum
    
# Time Complexity: O(N) where N is the length of the string.
# Space Complexity: O(min(M,N)) where M is the size of the character set and N is the length of the string.
# Explanation:
# 1. We use a sliding window approach with two pointers (left and right) to maintain a substring without repeating characters.
# 2. We use a dictionary to store the last seen position of each character.
# 3. As we expand the right pointer, if we encounter a repeating character, we move the left pointer to the right of the last seen position of that character.
# 4. We continuously update the maximum length of the substring found so far.