# Leetcode Problem 3202: find the Maximum Length of a Valid Subarray
# Difficulty : Medium
# Link : https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-ii/

# (Accepted solution)
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        res = 0
        dp = [[0]* k for _ in range(k)]
        for i in range(length):
            val = nums[i] %k
            for m in range(k):
                dp[val][m] = dp[m][val] + 1
                res = max(res, dp[val][m])
        return res

# Time complexity : O(N*K) where N is the number of elements in the input array and K is the given integer.     
# Space Complexity : O(K*K) as we are using a 2D array of size K*K.
# Explaination : the mod value will be same in alternate positions, so we can use a 2D array to store the maximum length of valid subsequence ending with a particular mod value.
# If we encounter the same mod value again, we can update the length of valid subsequence by adding 1 to the length of valid subsequence ending with the previous mod value.

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [[-1]*(k+1) for _ in range(length)]
        def validSubs(last_included_index, curr_index, mod):
            if(curr_index == length):
                return 0
            if(dp[last_included_index][mod] != -1):
                return dp[last_included_index][mod]
            include = 0
            if(mod == -1):
                if(last_included_index == -1):
                    # print("Included mod -1, l i : ", last_included_index, "C i : ", curr_index, "Mod : ", mod)
                    include = 1 + validSubs(curr_index, curr_index +1, -1)
                else:
                    # print("Include mod -1, l i : ", last_included_index, "C i : ", curr_index, "Mod : ", mod)
                    include = 1 + validSubs(curr_index, curr_index + 1, (nums[curr_index] + nums[last_included_index]) % k)
            else:
                if ((nums[curr_index] + nums[last_included_index]) % k) == mod:
                    # print("include : l i : ", last_included_index, "C i : ", curr_index, "Mod : ", mod)
                    include = 1 + validSubs(curr_index, curr_index + 1, mod)
            
            # print("Exclude : l i : ", last_included_index, "C i : ", curr_index, "Mod : ", mod)
            exclude = validSubs(last_included_index, curr_index + 1, mod)
            dp[last_included_index][mod] = max(include, exclude)
            return dp[last_included_index][mod]
        return validSubs(-1, 0, -1)
 