# Leetcode Problem 3637: Trionic Array 1
# Difficulty: Easy
# https://leetcode.com/problems/trionic-array-i/

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        length = len(nums)
        inc_flag1 = True
        dec_flag = False
        inc_flag2 = False
        for i in range(1,length):
            if(nums[i] == nums[i-1]):
                return False
            if(i == 1):
                if(nums[i] > nums[i-1]):
                    inc_flag1 = True
                else:
                    return False
            if(inc_flag1):
                if(nums[i] < nums[i-1]):
                    inc_flag1 = False
                    dec_flag = True
                    continue
            if(dec_flag):
                if(nums[i] > nums[i-1]):
                    inc_flag2 = True
                    dec_flag = False
                    continue
            if(inc_flag2):
                if(nums[i] < nums[i-1]):
                    return False
        if(inc_flag1 == False and dec_flag == False):
            return True
        else:
            return False
            
# Time complexity: O(n)
# The loop iterates through the list once, making it O(n).
# Space complexity: O(1)
# No additional space is used that scales with input size.
# The flags and counters are constant space.   