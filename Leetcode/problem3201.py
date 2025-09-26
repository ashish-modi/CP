# Leetcode Problem 3201: Maximum Length of Valid Subsequence 1
# Difficulty: Medium
# Link : https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/?envType=daily-question&envId=2025-07-16

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        length = len(nums)
        maximum = 0
        dp = [0]*length
        for i in range(length):
            dp[i] = nums[i]%2
        count_1 = count_0 = 0
        for i in range(length):
            if(dp[i] == 1):
                count_1 +=1
            else:
                count_0 +=1
        
        bit = 1
        alternate = 0
        for i in range(length):
            if(dp[i] == bit):
                bit = int(not bit)
                alternate +=1
        
        maximum = max(maximum, alternate, count_0, count_1)
        alternate = 0
        bit = 0
        for i in range(length):
            if(dp[i] == bit):
                bit = int(not bit)
                alternate +=1
        maximum = max(maximum, alternate)
        return maximum
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# where n is the length of the input array nums 