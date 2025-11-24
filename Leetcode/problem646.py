# Leetcode problem 646: Maximum Length of Pair Chain
# Difficulty: Medium
# Link: https://leetcode.com/problems/maximum-length-of-pair-chain/

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        length = len(pairs)
        pairs.sort(key= lambda x: x[1])
        right = pairs[0][1]
        left = pairs[0][0]
        chain = 1
        maximum = 1
        for i in range(1, length):
            l, r = pairs[i]
            if(l > right and l > left):
                chain +=1
                left = l
                right = r
            maximum = max(maximum, chain)
        return maximum
    
# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Explanation:
# 1. We sort the pairs based on their second element.
# 2. We iterate through the sorted pairs and check if the current pair can be added to the chain.
# 3. If it can be added, we increment the chain length and update the left and right boundaries.
# 4. We keep track of the maximum chain length and return it at the end.