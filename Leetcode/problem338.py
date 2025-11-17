# Leetcode Problem 338: Counting Bits
# Difficulty : Easy
# Link : https://leetcode.com/problems/counting-bits/
# Based on Dynamic Programming and Bit Manipulation

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        for i in range(n+1):
            ans[i] = bin(i).count('1')
        return ans

# Time Complexity : O(N) where N is the input number.
# Space Complexity : O(1) as we are using only constant space.
# Explanation:
# 1. We initialize an answer array of size n+1 with all elements set to 0.
# 2. We iterate through all numbers from 0 to n.
# 3. For each number, we convert it to its binary representation using the bin function and count the number of '1's using the count method.
# 4. We store the count of '1's in the answer array at the corresponding index.
# 5. Finally, we return the answer array containing the count of '1's for each number from 0 to n.