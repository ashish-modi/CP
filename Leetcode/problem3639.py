# Leeetcode problem 3639: Minimum Time to activate string
# Difficulty: Medium
# Link : https://leetcode.com/problems/minimum-time-to-activate-string/description/

class Solution:
    def binaryS(self, order, left, right, length, k):
        mid = (left + right)//2
        r = [1]*length
        for i in range(mid+1):
            r[order[i]] = 0
        total = 0
        count = 0
        for i in range(length):
            if(r[i]):
                count += r[i]
            else:
                total += (count * (count + 1))//2
                count = r[i]
        total += (count *(count +1)) // 2
        actual = (length * (length+1))//2
        
        if(left == right):
            if(actual - total >= k):
                return left
            else:
                return -1
        if(actual - total >= k):
            return self.binaryS(order, left, mid, length, k)
        else:
            return self.binaryS(order, mid + 1, right, length, k)
        


    def minTime(self, s: str, order: List[int], k: int) -> int:
        length = len(order)
        return self.binaryS(order, 0, length-1, length, k)

# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Explaination : 
# We use binary search to find the minimum time required to activate at least k characters in the string.
# We maintain a binary array to keep track of activated characters.
# For each mid value in binary search, we calculate the number of activated substrings and compare it with k.
# If the number of activated substrings is greater than or equal to k, we search in the left half, else we search in the right half.