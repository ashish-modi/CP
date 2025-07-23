# Problem : Maximum Erasure value (medium)

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        left = -1
        curr = 0
        maximum = 0
        dictionary = {}
        dp = [0]*length
        for i in range(length):
            dp[i] = nums[i] + dp[i-1]
            if(dictionary.get(nums[i],0)):
                if(left > dictionary[nums[i]]-1):
                    dictionary[nums[i]] = i+1
                else:
                    maximum = max(curr,maximum)
                    left = dictionary[nums[i]] -1
                    curr = dp[i] - dp[dictionary[nums[i]]-1]
                    dictionary[nums[i]] = i+1
                    continue
            else:
                dictionary[nums[i]] = i+1
            curr = dp[dictionary[nums[i]]-1] - dp[left]
        if(left == -1):
            curr = dp[-1]
        maximum = max(curr, maximum)
        return maximum
            