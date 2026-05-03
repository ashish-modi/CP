# Leetcode problem 560: Subarray Sum Equals K
# Difficulty: Medium
# URL : https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [0]*length
        count = {0:1}
        total = 0
        for i in range(length):
            dp[i] += dp[i-1] + nums[i]
            total += count.get(dp[i] - k, 0)
            if(dp[i] in count):
                count[dp[i]] +=1
            else:
                count[dp[i]] = 1
        return total
        
# Time complexity: O(n)
# Space complexity: O(n)
# Explanation: We use a dictionary to store the count of prefix sums. 
# For each prefix sum, we check if there is a prefix sum that is equal to the current prefix sum minus k. 
# If there is, we add the count of that prefix sum to the total count of subarrays that sum to k. 
# We also update the count of the current prefix sum in the dictionary.