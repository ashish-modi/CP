// Leetcode Problem 1143: Longest common subsequence
// Difficulty: Medium
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
public:
    int lcs(string text1, string text2, int index1, int index2, vector<vector<int>>& dp){
        
        if(index1 == 0 || index2 == 0){
            
            dp[index1][index2] = 0;
            return dp[index1][index2];
        }
        if(text1[index1-1] == text2[index2-1]){
            if(dp[index1][index2] == -1){
                int res = 1+ lcs(text1, text2, index1 -1, index2 -1, dp);
                dp[index1][index2] = res;
            }
            return dp[index1][index2];
        }

        if(dp[index1-1][index2] == -1){
            dp[index1 -1][index2] = lcs(text1, text2, index1 -1, index2, dp);
        }
        
        if(dp[index1][index2 -1] == -1){
            dp[index1][index2 -1] = lcs(text1, text2, index1, index2 -1, dp);
        }
        return max(dp[index1 -1][index2], dp[index1][index2-1]);
    }
    int longestCommonSubsequence(string text1, string text2) {
        int length1 = text1.size();
        int length2 = text2.size();
        vector<vector<int>> dp(length1 +1, vector<int> (length2+1, -1));
        dp[length1][length2] = lcs(text1, text2, length1, length2, dp);
        return dp[length1][length2];
    }
};

// Time Complexity : O(M*N) where M and N are the lengths of text1 and text2 respectively.
// Space Complexity : O(M*N) for the dp array.
// Explanation:
// 1. We define a recursive function `lcs` that takes the two strings, their current indices, and a dp array for memoization.
// 2. The base case checks if either index is 0; if so, we return 0.
// 3. If the characters at the current indices match, we add 1 to the result of the recursive call with both indices decremented.
// 4. If the characters do not match, we take the maximum of the results from two recursive calls: one with the first index decremented and the other with the second index decremented.
// 5. We store the results in the dp array to avoid redundant calculations.
// 6. The main function initializes the dp array and calls the `lcs` function with the lengths of the two strings.