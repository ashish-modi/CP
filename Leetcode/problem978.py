# Leetcode Problem 978: Longest Turbulent Subarray
# Difficulty: Medium
# URL: https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        sign_g = False
        sign_l = False
        count = 1
        maximum = 0
        if(length == 1):
            return length
        for i in range(length-1):
            if(not sign_g and not sign_l):
                if(arr[i] < arr[i+1]):
                    sign_g = True
                    count = 2
                elif(arr[i] > arr[i+1]):
                    sign_l = True
                    count = 2
                else:
                    count = 1
            else:
                if(sign_g):
                    if(arr[i] > arr[i+1]):
                        count +=1
                        sign_l = True
                        sign_g = False
                    elif(arr[i] < arr[i+1]):
                        count = 2
                        sign_g = True
                        sign_l = False
                    else:
                        sign_l = False
                        sign_g = False
                        count = 1
                else:
                    if(arr[i] < arr[i+1]):
                        count +=1
                        sign_g = True
                        sign_l = False
                    elif(arr[i] > arr[i+1]):
                        count = 2
                        sign_l = True
                        sign_g = False
                    else:
                        sign_l = False
                        sign_g = False
                        count = 1
                
            maximum = max(maximum, count)
        return maximum
    
# Time Complexity: O(N) where N is the length of the array.
# Space Complexity: O(1) as we are using a constant amount of extra space.
# Explanation:
# 1. We iterate through the array while maintaining two boolean flags to track the last comparison's direction (greater or less).
# 2. We count the length of the current turbulent subarray based on the comparisons and update the maximum length found so far.
# 3. If we encounter equal elements, we reset the count and flags.
# 4. Finally, we return the maximum length of the turbulent subarray found.
