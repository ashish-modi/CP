# Leetcode problem 122: Best Time to Buy and Sell Stock II
# Difficulty: Medium
# URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        curr = prices[0]
        total = 0
        for i in range(1,length):
            if(prices[i] < curr):
                curr = prices[i]
            else:
                total += prices[i] - curr
                curr = prices[i]
        return total
    
# Time complexity: O(n)
# Space complexity: O(1)
# Explaination: We can buy and sell the stock multiple times. 
# We can keep track of the current price and the total profit. 
# If the current price is less than the previous price, we can buy the stock. 
# If the current price is greater than the previous price, we can sell the stock and add the profit to the total. 
# We can repeat this process until we reach the end of the array.