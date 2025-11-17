# Leetcode Problem 3413: Maximum Coins from k consecutive bags
# Difficulty: Medium
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/




class Solution:
    def calculate(self, coins, length, k):

        maximum = 0
        prefix_sum = [0]*(length+ 1)
        for i in range(length):
            prefix_sum[i+1] = (abs(coins[i][1] - coins[i][0]) + 1)*coins[i][2] + prefix_sum[i]

        j = 0
        end = coins[0][1]
        size = maximum = interval = 0 
        for i in range(length):
            start = coins[i][0]
            if(j < i):
                j = i
                end = coins[j][1]
            while(j < length):
                size = abs(end - start) + 1
                interval = abs(coins[j][1] - coins[j][0]) + 1
                if( size <= k):
                    j+=1
                    if(j == length):
                        break
                    end = coins[j][1]
                else:
                    break
            j = min(j, length-1)
            current = prefix_sum[j] - prefix_sum[i]

            rem = min(interval - (size - k), interval)
            if(rem >0):
                current += rem* coins[j][2]
            if(current > maximum):
                maximum = current
            
            if(j == length):
                break
        return maximum

    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        length = len(coins)
        coins = sorted(coins)
        left = self.calculate(coins, length, k)
        test = [[-val[0],-val[1], val[2]] for val in coins]
        t = sorted(test)
        t = [[-val[1],-val[0], val[2]] for val in t]
        right = self.calculate(t, length, k)

        return max(left,right)

# Time complexity: O(n log n)
# The sorting takes O(n log n) and the two-pointer traversal takes O(n).
# Space complexity: O(n) for the prefix sum array.
# The space complexity is O(n) due to the storage of the prefix sum array.
# The overall complexity is O(n log n) due to the sorting step.
# The two-pointer traversal is linear, O(n), but the sorting dominates the time complexity.
# Explanation:
# The function calculates the maximum coins that can be collected from k consecutive bags.
# It uses a two-pointer technique to find valid intervals of bags that fit within the size k.
# The prefix sum array is used to efficiently calculate the total coins in the selected intervals.