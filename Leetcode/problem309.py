# Leetcode Problem: Best Time to Buy and Sell Stock with Cooldown
# Difficulty: Medium
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        dp = [[-1]*(2000) for _ in range(length + 1)]
        def count(curr_index, stock_price):
            if(curr_index >= length):
                return 0
            buy = 0
            sell = 0
            if(dp[curr_index][stock_price] != -1):
                return dp[curr_index][stock_price]

            if(stock_price == -1):
                buy = count(curr_index+1, stock_price + 1 + prices[curr_index])
                dont_buy = count(curr_index + 1, stock_price)
                buy = max(buy, dont_buy)
            diff = prices[curr_index] - stock_price
            if(stock_price > -1):
                if(diff > 0):
                    sell =  diff + count(curr_index+2, -1)
                    dont_sell = count(curr_index+1, stock_price)
                    sell = max(sell, dont_sell)

            dp[curr_index][stock_price] = buy + sell
            return dp[curr_index][stock_price]
        
        return count(0, -1)


# Time Complexity: O(n * 2000)
# Space Complexity: O(n * 2000)
# Note: This is a recursive solution with memoization to find the maximum profit from stock trading with a cooldown period.
# The solution uses dynamic programming to store intermediate results in a 2D array `dp`, where `dp[i][j]` represents the maximum profit achievable starting from day `i` with a stock price of `j`.
# The function `count` recursively explores both buying and selling the stock, considering the cooldown period after a sale.
# The base case checks if the current index exceeds the length of the prices list, returning 0 in that case.
# The function returns the maximum profit that can be achieved by making optimal buy and sell decisions while adhering to the cooldown constraint.