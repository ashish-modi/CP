# Leetcode Problem 658 : Find K closest elements
# Difficulty : Medium
# URL : https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        length = len(arr)
        left = right = total = 0
        left_b = right_b = 0
        result = float('inf')
        while(right - left + 1 < k):
            total += abs(arr[right] - x)
            right +=1
        result = total
        left_b = left
        right_b = right
        while(right < length-1):
            first = abs(arr[left] - x)
            left +=1 
            right +=1
            last = abs(arr[right] - x)
            total -= first 
            total += last
            if(total < result):
                result = total
                left_b = left
                right_b = right
        return arr[left_b: right_b + 1]
            
            
# Time complexity : O(n)
# Space complexity : O(1)
# Explaination : We use a sliding window approach to find the k closest elements to x. 
# We maintain a window of size k and slide it through the array to find the window with the minimum sum of absolute differences.
