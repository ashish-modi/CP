// Leetcode Problem 300 : Longest Increasing subsequence 
// Difficulty: Medium
// https://leetcode.com/problems/longest-increasing-subsequence/


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

// Time Complexity : O(N^2) where N is the number of elements in the input array.
// Space Complexity : O(N^2) for the dp array.
// Explanation:
// 1. We define a recursive function LIS that takes the current index, the last included index, and a dp array for memoization.
// 2. The base case checks if the current index is greater than or equal to the size of the input array; if so, we return 0.
// 3. We check if the result for the current index and last included index is already computed in the dp array; if so, we return that value.
// 4. We calculate the length of the longest increasing subsequence by either including or excluding the current element.
// 5. We store the maximum of the two options in the dp array and return it.
// 6. The main function initializes the dp array and calls the LIS function starting from index 0 and last included index