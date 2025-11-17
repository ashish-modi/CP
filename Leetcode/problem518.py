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
# Explanation:
# 1. We define a recursive function `count` that takes the current index of the coin and the remaining amount as parameters.
# 2. The base case checks if the remaining amount is zero, in which case we have found a valid combination and return 1.
# 3. If the remaining amount is negative or we have exhausted all coins, we return 0.
# 4. We use a dp array to store intermediate results to avoid redundant calculations.
# 5. We explore both including the current coin (by not moving to the next index) and excluding it (by moving to the next index).
# 6. The function returns the total number of combinations that sum up to the target amount.
# the target amount using the given coins.