# Leetcode problem 3755: Maximum Length of a Balanced Subarray
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-length-of-a-balanced-subarray/

class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        result = 0
        diff = 0
        dictionary = {'0#0' : (-1,-1)}
        r = 0
        for i in range(length):
            r ^= nums[i]
            if(nums[i]%2 == 0):
                diff +=1
            else:
                diff -=1
            pattern = str(r) + "#" + str(diff)
            if(dictionary.get(pattern,0)):
                _, index = dictionary[pattern]
                result = max(result, i - index)
            else:
                dictionary[pattern] = (i,i)
        return result
    
# Time Complexity: O(n)
# Space Complexity: O(n)
# Explanation:
# 1. We use a dictionary to store the first occurrence of each (parity, diff) pair.
# 2. We iterate through the array, updating the parity and diff values.
# 3. For each (parity, diff) pair, we check if it has been seen before.
# 4. If it has, we calculate the length of the subarray and update the result if it's longer than the previous maximum.
# 5. If it hasn't been seen, we store the current index as the first occurrence.
# 6. Finally, we return the maximum length of the balanced subarray found.