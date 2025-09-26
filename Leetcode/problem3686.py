# Leetcode Problem: 3686. Count Stable Subsequences
# Difficulty: Hard
# https://leetcode.com/problems/count-stable-subsequences/


class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        length = len(nums)
        one_odd = two_odd = one_even = two_even = 0
        MOD = 10**9+7
        for i in range(length):
            if(nums[i] % 2 == 0):
                two_even += one_even
                two_even %= MOD
                one_even += one_odd + two_odd + 1
                one_even %= MOD
            else:
                two_odd += one_odd
                two_odd %= MOD
                one_odd += one_even + two_even + 1
                one_odd %= MOD
        return (one_odd + one_even + two_odd + two_even) % MOD
    
# Time complexity: O(n)
# Space complexity: O(1)