# Leetcode Problem 167: Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# URL: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length =len(numbers)
        left = 0
        right = length-1
        while(left <= right):
            val = numbers[left] + numbers[right]
            if(val == target):
                return [left+1, right+1]
            if(val < target):
                left +=1
            else:
                right -=1
        
# Time complexity:
# O(N) - In the worst case, we may need to traverse the entire array with the two pointers.
# Space complexity:
# O(1) - We use only a constant amount of extra space for the two pointers.
# Explanation:
# The solution uses the two-pointer technique to find two numbers that add up to the target. 
# Since the input array is sorted, we can start with one pointer at the beginning (left) and another at the end (right) of the array. 
# Depending on whether the sum of the two numbers is less than, greater than, or equal to the target, we adjust the pointers accordingly until we find the correct pair.