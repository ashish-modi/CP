# Leetcode Problem 41: First Missing Positive
# Difficulty: Hard
# URL: https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        dictionary = {}
        for i in range(length):
            dictionary[nums[i]] = dictionary.get(nums[i],0) + 1
        for i in range(1,length+2):
            if(not dictionary.get(i,0)):
                return i
            
# Time complexity:
# O(N) - We traverse the list of numbers once to build the dictionary and then again to find the first missing positive integer.
# Space complexity:
# O(N) - We use a dictionary to store the presence of numbers, which in the worst case can store all N numbers.
# Explanation:
# The solution uses a dictionary to keep track of the numbers present in the input list.
# We first populate the dictionary with all numbers from the list.
# Then, we iterate from 1 to N+1 (where N is the length of the list) to find the smallest positive integer that is not present in the dictionary.
# The first missing positive integer is returned as the result.