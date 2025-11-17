# Leetcode Problem 15: 3Sum
# Difficulty: Medium
# URL: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        res = []
        for i in range(length):
            if(i> 0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = length -1
            find = -nums[i]
            while(left < right):

                curr_val = nums[left] + nums[right]
               
                if(left == i):
                    left +=1
                    continue
                if(right == i):
                    right -=1
                    continue
                
                if(curr_val == find):    
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right -=1
                    while(left < right and nums[left] == nums[left-1]):
                        left +=1
                    while(left < right and nums[right] == nums[right+1]):
                        right -=1
                elif(curr_val < find):
                    left +=1
                else:
                    right -=1
        return res
    

# Time complexity:
# O(N^2) - We sort the array (O(N log N)) and then use a nested loop (O(N^2)) to find triplets, resulting in an overall time complexity of O(N^2).
# Space complexity:
# O(1) - We use a constant amount of extra space for variables, not counting the output list.
# Explanation:
# The solution first sorts the input array to facilitate the two-pointer technique. 
# For each element in the array, it uses two pointers to find pairs that sum up to the negative of the current element. 
# It also includes checks to skip duplicate elements to ensure that the output contains unique triplets only.