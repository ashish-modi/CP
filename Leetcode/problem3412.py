# Leetcode Problem 3412: Find Mirror Score of a String
# Difficulty: Medium
# https://leetcode.com/problems/find-mirror-score-of-a-string/description/

class Solution:
    def calculateScore(self, s: str) -> int:
        score = 0
        length = len(s)
        dictionary = {i: deque() for i in range(97, 123)}
        for i in range(length):
            ascii = ord(s[i])
            rev = 122 - (ascii - 97)
            if(dictionary[rev]):
                index = dictionary[rev].popleft()
                score += i - index
            else:
                dictionary[ascii].appendleft(i)
        return score
    
# Time complexity: O(n)

# Inside the loop:
# ord(s[i]): O(1)
# Compute rev: O(1)
# if(dictionary[rev]): O(1) (check if deque is non-empty)
# dictionary[rev].popleft(): O(1)
# dictionary[ascii].appendleft(i): O(1)