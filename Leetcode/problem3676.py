# Leetcode Problem 3676: Count Bowl Subarrays
# Difficulty : Medium
# Link : https://leetcode.com/problems/count-bowl-subarrays/    
# Based on Monotonic Stack Approach

class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        length = len(nums)
        right = [-1]*length
        result = 0
        stack = deque()
        for i in range(length):
            while(stack and (nums[i] > nums[stack[-1]])):
                index = stack.pop()
                right[index] = i        
            stack.append(i)
                    
        stack = deque()
        left = [-1]*length
        for i in range(length-1, -1, -1):
            while(stack and (nums[i] > nums[stack[-1]])):
                index = stack.pop()
                left[index] = i        
            stack.append(i)
    
        for i in range(length):
            if(right[i] != -1 and (right[i] - i + 1) > 2):
                result +=1
            if(left[i] != -1 and (i - left[i] + 1)> 2):
                result +=1
        return result



# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(N) as we are using extra space for left and right arrays.    
# Explanation : The solution uses a monotonic stack approach to find the nearest greater elements to the left and right of each element in the array. 
# It then counts the number of bowl subarrays based on these indices.