# Leetcode problem 875: Koko Eating Bananas
# Difficulty: Medium
# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        minimum = maximum = piles[0]
        for i in range(1, length):
            if(piles[i] < minimum):
                minimum = piles[i]
            if(piles[i] > maximum):
                maximum = piles[i]
        def check_mid(num):
            total = 0
            for i in range(length):
                q = piles[i] // num
                r = piles[i] % num
                total += q + 1 if r else q
            return True if(total <= h) else False
        answer = 0
        left, right = 1, maximum
        while(left <= right):
            mid = (left + right) //2
            if(check_mid(mid)):
                answer = mid 
                right = mid -1
            else:
                left = mid + 1
        
        return answer
        
# Time complexity: O(n log m), where n is the length of piles and m is the maximum number of bananas in a pile.
# Space complexity: O(1)
# Explaination : We can use binary search to find the minimum eating speed. 
# We start with the minimum speed of 1 and the maximum speed of the largest pile. We check if the current speed is sufficient to eat all the bananas within h hours. 
# If it is, we can try a smaller speed, otherwise we need to increase the speed. 
# We continue this process until we find the minimum speed that allows Koko to eat all the bananas within h hours.