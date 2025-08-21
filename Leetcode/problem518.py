# Leetcode Problem: Coin Change II
# Difficulty: Medium
# Link: https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        length = len(coins)
        dp = [[-1] *(amount+1) for _ in range(length+1)]
        def count(curr_index, rem_amount):
            if(rem_amount == 0):
                return 1
            if(rem_amount < 0 or curr_index == length and rem_amount > 0):
                return 0
            if(dp[curr_index][rem_amount] != -1):
                return dp[curr_index][rem_amount]

            include = count(curr_index, rem_amount - coins[curr_index])
            exclude = count(curr_index + 1, rem_amount)
            dp[curr_index][rem_amount] = include + exclude

            return dp[curr_index][rem_amount]

        return count(0, amount)
    
# Time Complexity: O(n * amount)
# Space Complexity: O(n * amount)
# Note: This is a recursive solution with memoization to count the number of ways to make