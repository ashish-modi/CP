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