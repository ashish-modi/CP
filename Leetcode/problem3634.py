# Leetcode Problem 3634: Minimum Removals to balance array
# Difficulty: Medium
# https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution:
    def bsearch(self, arr, left, right, target,k):
        if(left > right):
            return -1
        mid = (left + right) //2
        total = target*k
        if(arr[mid] > total and arr[mid-1] <= total):
            return mid
        elif(arr[mid] <= total):
            return self.bsearch(arr, mid + 1, right, target, k)
        else:
            return self.bsearch(arr, left, mid-1, target, k)

    def minRemoval(self, nums: List[int], k: int) -> int:
        length = len(nums)
        sorted_list = sorted(nums)
        minimum = float('inf')
        for i in range(length):
            count = i
            index = self.bsearch(sorted_list, i+1, length-1, sorted_list[i], k)
            if(index != -1):
                val =  length - index
                count += val
            if(count < minimum):
                minimum = count
        return minimum
    
# Time complexity: O(n log n)
# The sorting takes O(n log n) and the binary search takes O(log n) for each element, leading to an overall complexity of O(n log n).
# Space complexity: O(n) for the sorted list.
# The space complexity is O(n) due to the storage of the sorted list.
# Explaination:
# The solution involves sorting the array and then using binary search to find the minimum number of removals needed to balance the array.
# For each element in the sorted array, we calculate how many elements need to be removed to ensure that no element is more than k times another element.
# We keep track of the minimum removals required and return that value at the end.