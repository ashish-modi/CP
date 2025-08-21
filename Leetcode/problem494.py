# Leetcode Problem: Target Sum
# Difficulty: Medium
# Link: https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)
        maximum = abs(max(nums))*length
        dp = [[-1]* (abs(target)+maximum+1) for _ in range(length+1)]
        def count(curr_index, curr_target):
            if(curr_index == length):
                return 1 if curr_target == 0 else 0
            if(dp[curr_index][curr_target] != -1):
                return dp[curr_index][curr_target]

            plus = count(curr_index +1, curr_target + nums[curr_index])
            minus = count(curr_index + 1, curr_target - nums[curr_index])

            dp[curr_index][curr_target] = plus + minus
            return dp[curr_index][curr_target]

        return count(0, target)

# Time Complexity: O(n * (target + maximum))
# Space Complexity: O(n * (target + maximum))
# Note: This is a recursive solution with memoization to count the number of ways to assign signs to numbers in an array such that their sum equals a target value.
# The solution uses dynamic programming to store intermediate results in a 2D array `dp`, where `dp[i][j]` represents the number of ways to achieve a sum `j` using the first `i` elements of `nums`.
# The function `count` recursively explores both adding and subtracting the current number, updating the `dp` array to avoid redundant calculations.
# The base case checks if all numbers have been processed and whether the current target sum is zero, returning 1 if true and