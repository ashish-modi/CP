


// TLE Solution
class Solution {
public:
    int LIS(vector<int>& nums, vector<vector<int>>& dp, int curr_index, int last_index, int difference){
        // cout << "Current index : " << curr_index << " Last index : " << last_index << " Diff : " << difference << endl;
        if(curr_index == nums.size()){
            // cout << "returning 0" << endl;
            return 0;
        }

        // if(dp[curr_index][last_index + 1] != -1){
        //     cout << " Returning DP : " << endl;
        //     return dp[curr_index][last_index + 1];
        // }
        int include = 0;
        if(last_index == -1 || abs(nums[curr_index] - nums[last_index]) <= difference){
            // cout << "Including : " << nums[curr_index] << endl;
            if(last_index == -1){
                include = 1+ LIS(nums, dp, curr_index + 1, curr_index, difference);
            }
            else{
                // cout << "Difference : " << abs(nums[curr_index] - nums[last_index]) << endl;
                include = 1+ LIS(nums, dp, curr_index + 1, curr_index, abs(nums[curr_index] - nums[last_index]));
            }
        }
        // cout << "Excluding : " << nums[curr_index] << endl;
        int exclude = LIS(nums, dp, curr_index + 1, last_index, difference);
        
        dp[curr_index][last_index + 1] = max(include, exclude);
        // cout << "Current index : " << curr_index << " Last index : " << last_index << " Diff : " << difference << "  Include : "<< include << " Exclude : " << exclude << endl;
        return max(include,exclude);
        return dp[curr_index][last_index + 1];
    }
    int longestSubsequence(vector<int>& nums) {
        int length = size(nums);
        vector<vector<int>> dp (length, vector<int>(length+1, -1));
        int res = LIS(nums, dp, 0, -1, 400);

        // for(auto row : dp){
        //     for(auto ele: row){
        //         cout << ele << " ";
        //     }
        //     cout << endl;
        // }
        return res;
    }
};