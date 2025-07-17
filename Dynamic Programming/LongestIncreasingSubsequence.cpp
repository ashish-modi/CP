// Using recursion

class Solution {
public:
    int LIS(vector<int>& nums, int index, vector<vector<int>>& dp, int last_included){
        if(index >= size(nums)){
             return 0;
        }
        if(dp[index][last_included+1] != -1)
            return dp[index][last_included + 1];

        int include = 0;
        if(last_included == -1 || nums[index] > nums[last_included])
            include = 1  + LIS(nums, index + 1, dp, index);
        int exclude = LIS(nums, index + 1, dp , last_included);

        return dp[index][last_included +1] = max(include, exclude);
    }
    int lengthOfLIS(vector<int>& nums) {
        int length = nums.size();
        vector<vector<int>> dp(length+1, vector<int>(length+1,-1));
        return LIS(nums, 0, dp, -1);
        
        // for(int i = 0; i < length+1; i++){
        //     dp[length][0] = 0;
        //     dp[0][length] = 0;
        // }
        // for(auto row: dp){
        //     for(auto ele : row)
        //         cout << ele << " ";
        //     cout << endl;
        // }
    }
};