# Leetcode Problem 3147: Maximum Energy You Can Obtain from Cards
# Difficulty: Medium
# URL: https://leetcode.com/problems/maximum-energy-you-can-obtain-from-cards/

class Solution:
    
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        length = len(energy)
        maximum = float('-inf')
        dp = [float('-inf')]*(length + k)
        i = length -1
        while(i > -1):
            if(i > length-1-k):
                dp[i] = energy[i]
            else:
                
                dp[i] = dp[i+k] + energy[i]
            i-=1
        
        return max(dp)
        


# Time complexity:
# O(N) - We iterate through the energy list once to fill the dp array.
# Space complexity:
# O(N) - We use an additional dp array of size N + k to store the maximum energy values.
# Explanation:
# The solution uses dynamic programming to calculate the maximum energy that can be obtained by picking cards. 
# We create a dp array where dp[i] represents the maximum energy obtainable starting from the i-th card. 
# We fill this array in reverse order, considering the energy of the current card.