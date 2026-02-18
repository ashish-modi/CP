# Problem 912 : Sort an Array
# Difficulty : Medium
# URL : https://leetcode.com/problems/sort-an-array/

class Solution:
    def merge(self,left, right):
        l1 = len(left)
        l2 = len(right)
        i = j = 0
        res = []
        while(i < l1 and j < l2):
            if(left[i] < right[j]):
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if(i == l1):
            while(j < l2):
                res.append(right[j])
                j+=1
        else:
            while(i < l1):
                res.append(left[i])
                i+=1
        return res

    def merge_sort(self,left, right, nums):
        if(left == right):
            return [nums[left]]
        mid = (left + right) //2
        left_arr = self.merge_sort(left, mid, nums)
        right_arr = self.merge_sort(mid+1, right, nums)
        return self.merge(left_arr, right_arr)

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(0, len(nums) -1, nums)
    
# Time complexity : O(n log n)
# Space complexity : O(n)
# Explanation :
# The algorithm uses the merge sort technique to sort the array. 
# It recursively divides the array into two halves until it reaches individual elements, 
# then merges the sorted halves back together in a sorted manner.