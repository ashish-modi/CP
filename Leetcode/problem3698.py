# Leetcode Problem 3698: Split Array with minimum difference
# Difficulty : Medium
# Link : https://leetcode.com/problems/split-array-with-minimum-difference/
# Based on Dynamic Programming

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        length = len(nums)
        flag = 0
        inc = 1
        dec = once = 0
        dp = [0]*length
        pivot = -1
        if(length == 2):
            
            return abs(nums[0]-nums[1])

        for i in range(length):
            dp[i] = dp[i-1] + nums[i]
        total = dp[-1]
        for i in range(1,length):
            if(nums[i] <= nums[i-1]):
                pivot = i-1
                break
                
        if(pivot != -1):
            for i in range(pivot+1, length-1):
                if(nums[i] <= nums[i+1]):
                    return -1
        
        if(pivot == -1):
            return total - 2*nums[-1]
        if pivot > 0:
            return min(abs(2 * dp[pivot] - total), abs(2 * dp[pivot-1] - total))
        else:
            return abs(2 * dp[pivot] - total)
        
# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(N) as we are using extra space for dp array.
# Note : The problem can be solved using Dynamic Programming approach. The idea is to find the pivot point where the array can be split into two parts such that the difference between the sum of the two parts is minimized. The pivot point is the point where the array stops being non-increasing and starts being non-decreasing. 
# If there is no such point, then the array is either entirely non-increasing or non-decreasing.
# In that case, we can simply return the absolute difference between the total sum and twice the last element (if non-decreasing) or the first element (if non-increasing). 
# If there is a pivot point, we can calculate the sum of the left part and the right part and return the minimum absolute difference between the two parts.