# Leetcode Problem 3685: Subsequence Sum After Capping
# Difficulty: Medium
# https://leetcode.com/problems/subsequence-sum-after-capping/


class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        length = len(nums)
        nums.sort()
        dp = [False]*(k+1)
        dp[0] = True
        result = [False]*length
        j = 0
        
        for i in range(length):    # represents day
            while(j < length and nums[j] < i+1):
                
                for m in range(k, nums[j]-1, -1):
                    dp[m] = dp[m] or dp[m - nums[j]]
                    
                j+=1
            greater = length - j
            
            for t in range(greater+1):
                val = k - (i+1)*t
                if(val >= 0 and dp[val]):
                    result[i] = True
    
            
        return result

# Time Complexity: O(n*k)
# Space Complexity: O(k)
# where n is the length of nums and k is the given integer k.   