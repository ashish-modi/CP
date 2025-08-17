class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        pre_prod = [1]*(length+1)
        for i in range(1,length+1):
            pre_prod[i] = pre_prod[i-1] * nums[i-1]
        # print("PRE prod : ", pre_prod)
        dp = [[1]*length for _ in range(length)]
        maximum = 0
        for i in range(length):
            for j in range(i, length):
                dp[i][j] = pre_prod[j+1] // (pre_prod[i] if pre_prod[i] else 1)
                maximum = max(dp[i][j], maximum)
                    
        # for row in dp:
        #     print(row)
        return maximum