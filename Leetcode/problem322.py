#  Leetcode Problem 322: Coin Change
#  Difficulty Level: Medium
#  Problem Link: https://leetcode.com/problems/coin-change/

class Solution:
    def makeChange(self, coins, dp, curr_index, amount, length):
        if(curr_index == length and amount != 0):
            return (False, -1)
        if(amount == 0):
            return (True, 0)
        if(dp[curr_index][amount] != -1):
            return dp[curr_index][amount]

        t_f_inc1 = False
        t_f_inc2 = False
        include1 = 0
        include2 = 0
        if(amount >= coins[curr_index]):
            t_f_inc1, include1 = self.makeChange(coins, dp, curr_index, amount - coins[curr_index], length)
            t_f_inc2, include2 = self.makeChange(coins, dp, curr_index + 1, amount - coins[curr_index], length)
            include1 +=1
            include2 +=1
        
        t_f_exc, exclude = self.makeChange(coins, dp, curr_index + 1, amount, length)
        inc1 = include1 if(t_f_inc1) else float('inf')
        inc2 = include2 if(t_f_inc2) else float('inf')
        exc = exclude if(t_f_exc) else float('inf')

        dp[curr_index][amount] =  (t_f_inc1 or t_f_inc2 or t_f_exc, min(inc1, inc2, exc))
        return dp[curr_index][amount]
            

    def coinChange(self, coins: List[int], amount: int) -> int:
        length = len(coins)
        dp = [[-1]*10001 for _ in range(length)]
        t_f, value = self.makeChange(coins, dp, 0, amount, length)
        return value if t_f else -1

#  Time Complexity: O(n * amount) where n is the number of coins
#  Space Complexity: O(n * amount) for the dp array
#  Note: The code uses recursion with memoization to efficiently find the minimum number of coins needed to make the given amount.
#  The function returns -1 if it's not possible to make the amount with the given coins.
#  The algorithm explores both including and excluding each coin, ensuring all combinations are considered.