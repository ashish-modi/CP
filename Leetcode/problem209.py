# Leetcode problem 209: Minimum Size Subarray Sum
# Difficulty: Medium
# URL : https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        length = len(nums)
        left = 0
        right = 1
        dp = [0]*(length+1)
        for i in range(1,length+1):
            dp[i] = dp[i-1] + nums[i-1]
        while True:
            if(right == length+1):
                break
            while(dp[right] - dp[left] >= target):
                if(right - left < min_length):
                    min_length = right - left
                left +=1
            right +=1
            
        return 0 if min_length == float('inf') else min_length
    
# Time complexity: O(n)
# Space complexity: O(n)
# Explaination:
# We can use two pointers to solve this problem. We can use a dp array to store the sum of the elements from the left pointer to the right pointer. 
# We can move the right pointer to the right until the sum is greater than or equal to the target. 
# Then we can move the left pointer to the right until the sum is less than the target. 
# We can update the minimum length of the subarray at each step.