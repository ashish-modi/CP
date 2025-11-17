# Leetcode Problem 416: Partition Equal Subset Sum  
# Difficulty Level: Medium
# Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def partition(self, nums, dp, length, curr_index, curr_sum, total):
        if(curr_sum > total or curr_index == length and curr_sum != total):
            return False
        if(curr_sum == total):
            return True
        if(dp[curr_index][curr_sum] != -1):
            return dp[curr_index][curr_sum]

        include = self.partition(nums, dp, length, curr_index + 1, curr_sum + nums[curr_index], total)
        exclude = self.partition(nums, dp, length, curr_index + 1, curr_sum, total)

        dp[curr_index][curr_sum] =  include or exclude
        return dp[curr_index][curr_sum]


    def canPartition(self, nums: List[int]) -> bool:
        length = len(nums)
        total = sum(nums)
        if(total % 2):
            return False
        dp = [[-1]*20001 for _ in range(length)]
        return self.partition(nums, dp, length, 0, 0, total//2)
        
# Time Complexity: O(n * total) where n is the number of elements in nums and total is the sum of elements
# Space Complexity: O(n * total) for the dp array
# Note: The code uses recursion with memoization to efficiently check if the array can be partitioned into two subsets with equal sum.
# The function returns True if such a partition exists, otherwise returns False.
# Explanation:
# 1. We define a recursive function `partition` that takes the current index, current sum, and total sum as parameters.
# 2. The base cases check if the current sum exceeds the total or if we have reached the end of the array without achieving the target sum.
# 3. We use a dp array to store intermediate results to avoid redundant calculations.
# 4. We explore both including and excluding the current element in the subset.
# 5. The main function initializes the dp array and calls the partition function starting from index 0 and current sum 0