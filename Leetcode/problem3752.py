# LeetCode Problem 3752: Lexicographically Smallest Negated Permutation that Sums to Target
# Difficulty: Medium
# https://leetcode.com/problems/lexicographically-smallest-negated-permutation-that-sums-to-target/

class Solution:
    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
        max_sum = (n*(n+1)//2)
        if(target > max_sum or target < -max_sum):
            return []
        res = list(range(1, n+1))
        total = max_sum
        for i in range(n-1, -1, -1):
            if(total - 2*res[i] >= target):
                total -= 2*res[i]
                res[i] = -res[i]
            if(total == target):
                break
        res.sort()
        return res if total == target else []
            
        
# Time complexity: O(n log n)
# The sorting step takes O(n log n) time, and the rest of the operations are O(n).
# Space complexity: O(n)
# The space complexity is O(n) due to the storage of the result array.
# Explaination:
# The solution first checks if the target is achievable given the maximum possible sum of the first n natural numbers.
# It then iterates from the largest number to the smallest, negating numbers as long as it helps to reach the target sum.
# Finally, it sorts the resulting array to ensure it is in lexicographically smallest order before returning it.

