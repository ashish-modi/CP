# Leetcode 3409. Longest Arithmetic Subsequence With Decreasing Adjent Difference
# Difficulty: Medium
# https://leetcode.com/problems/longest-arithmetic-subsequence-with-decreasing-adjent-difference/

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        dp = [[0]*302 for _ in range(302)]
        length = len(nums)
        ans = 0
        for i in range(length):
            maximum = 0
            for j in range(300,-1,-1):      # difference
                l = nums[i] - j
                g = nums[i] + j
                curr = 0
                if l >= 0:
                    tmp = 1 + dp[l][j]
                    curr = max(curr, tmp)
                if( g <= 300):
                    tmp = 1 + dp[g][j]
                    curr = max(curr, tmp)
                maximum = max(maximum, curr)
                dp[nums[i]][j] = maximum
                ans = max(ans, maximum)
        return ans
    
# Time complexity: O(N*D) where N is the length of nums and D is the range of difference (300 here)
# Space complexity: O(N*D) where N is the length of nums and D is the range of difference (300 here)
# Explanation : x, y and z are three consecutive elements in the subsequence.
# Then, the difference between x and y must be greater than the difference between y and z.
# So, if the difference between x and y is d, then the difference between y and z must be less than d.
# So, we can use dynamic programming to store the length of the longest subsequence ending at each element with a given difference.
# We iterate through the array and for each element, we check all possible differences from 0 to 300.
# For each difference, we check if there exists a previous element such that the difference between the current element and the previous
# element is equal to the current difference. If such an element exists, we update the dp table and the answer accordingly. 