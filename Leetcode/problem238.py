# Problem 238: Product of Array Except Self
# Difficulty: Medium
# URL: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        dp = [1]*(length+1)
        count_zeros = 0
        prod = 1
        res = [0]*length
        for i in range(length):
            if(nums[i]):
                prod = nums[i]*prod
            else:
                count_zeros +=1
        for i in range(length):
            if(nums[i] == 0):
                if(count_zeros >1):
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                if(count_zeros):
                    res[i] = 0
                else:
                    res[i] = prod // nums[i]
        return res

# Time complexity: O(N) where N is the length of the input array nums.
# Space complexity: O(1) if we don't count the output array, otherwise O(N) for the output array.
# Explanation: The solution first calculates the product of all non-zero elements in the input array and counts the number of zeros.
# It then iterates through the array again to fill the result array based on the number of zeros found.
# If there are more than one zero, all products will be zero. If there is one zero, only the position of that zero will have the product of all other elements, and all other positions will be zero.
# If there are no zeros, each position in the result array is filled with the total product divided by the element at that position.