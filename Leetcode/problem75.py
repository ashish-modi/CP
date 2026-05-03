# Leetcode Problem 75 : Sort Colors
# Difficulty : Medium
# URL : https://leetcode.com/problems/sort-colors/description/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr +=1
        
        last = ptr
        for i in range(ptr, len(nums)):
            if(nums[i] == 1):
                nums[i], nums[last] = nums[last], nums[i]
                last +=1
        return nums
    
# Time Complexity : O(n)
# Space Complexity : O(1)
# Explaination : The algorithm uses two pointers to partition the array into three sections: 0s, 1s, and 2s. 
# It first places all 0s at the beginning, then all 1s in the middle, and finally all 2s at the end.