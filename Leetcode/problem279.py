# Leetcode Problem 279: Perfect Squares
# Difficulty: Medium
# URL: https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}
        def max_sq(num: int) -> int:
            if(num == 0):
                return 0
            minimum = float('inf')
            if(num in dp):
                return dp[num]
            for i in range(1, num+1):
                if(i*i > num):
                    break        
                res = 1 + max_sq(num - i*i)
                minimum = min(minimum, res)
            dp[num] = minimum
            return minimum
        return max_sq(n)
    
# Time Complexity: O(n * sqrt(n))
# Space Complexity: O(n)
# Explanation:
# The function numSquares uses a helper function max_sq to compute the minimum number of perfect squares
# that sum up to the integer n. It employs memoization to store previously computed results in the dp dictionary,
# which helps to avoid redundant calculations. The max_sq function recursively explores all possible perfect squares
# that can be subtracted from the current number and calculates the minimum count for each subtraction. 
# The base case is when the number is 0, which returns 0. The final result is obtained by calling max_sq with the input n.