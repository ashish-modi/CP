# Leetcode problem 1186: Maximum Subarray Sum with One Deletion
# Difficulty : Medium
# Link : https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
    
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        length = len(arr)
        dp_f = [float('-inf')]*(length+1)
        dp_b = [float('-inf')]*(length+1)
        for i in range(length):
            dp_f[i] = max(dp_f[i-1] + arr[i], arr[i])
        for i in range(length-1, -1, -1):
            dp_b[i] = max(dp_b[i+1] + arr[i], arr[i])
        maximum = max(max(dp_f), max(dp_b))
       
        for i in range(1, length-1):
            maximum = max(maximum, dp_f[i-1] + dp_b[i+1])
        return maximum

                
# Time Complexity : O(N) where N is the number of elements in the input array.
# Space Complexity : O(N) where N is the number of elements in the input array as we are using two dp arrays of size N.
# Explaination :
# The function maximumSum takes a list of integers arr as input and returns the maximum subarray sum with one deletion allowed.
# It uses two dynamic programming arrays, dp_f and dp_b, to store the maximum subarray sums ending at each index from the front and back respectively.
# It first fills these arrays by iterating through the input array.
# Then, it calculates the maximum subarray sum by considering both the cases of no deletion and one deletion, and returns the maximum value found.
# Traverse the array and consider the ith element as deleted and calculate the maximum sum by adding the maximum sum subarray ending before i and starting after i.